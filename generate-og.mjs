// Regenerates Asset/og-image.png by screenshotting the real hero, so the share
// card can never drift from the page. Run with: node generate-og.mjs
//
// It renders index.html with a few overrides that only affect the 1200x630 crop:
// the books grow a little and their spine text shrinks, so every chapter title
// fits on its spine at card size instead of being clipped.

import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));

const CHROME = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => { try { readFileSync(p); return true; } catch { return false; } });

if (!CHROME) throw new Error('No Chrome or Edge binary found — edit the CHROME list above.');

const OVERRIDES = `
/* OG render overrides: sized for a 1200x630 share card */
.shelf-stage{--book-max:180px;padding-bottom:8px}
.book{min-height:156px}
.book .spine-label{font-size:.52rem;max-height:88%}
.hero-center{padding-top:12px}
`;

const work = mkdtempSync(join(tmpdir(), 'og-'));
const page = join(work, 'og-src.html');
const html = readFileSync(join(root, 'index.html'), 'utf8');
writeFileSync(page, html.replace('</style>', `${OVERRIDES}</style>`));

const out = join(root, 'Asset', 'og-image.png');
execFileSync(CHROME, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
  '--force-prefers-reduced-motion',   // freeze the nudging scroll arrow
  '--force-device-scale-factor=2',    // 2400x1260, crisp on retina
  '--virtual-time-budget=9000',       // let the Google fonts land
  '--window-size=1200,630',
  `--screenshot=${out}`,
  `file://${page.replace(/\\/g, '/')}`,
], { stdio: 'inherit' });

rmSync(work, { recursive: true, force: true });
console.log(`Wrote ${out}`);
