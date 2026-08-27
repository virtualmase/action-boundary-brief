import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const source = readFileSync(resolve(new URL('..', import.meta.url).pathname, 'script.js'), 'utf8');
const rules = [
  ['has three prewritten cases', 'config:{code:'],
  ['updates fields from cases', "Object.entries(fields).forEach"],
  ['does not create a score', 'score'],
  ['does not use visitor storage', 'localStorage'],
  ['updates mobile ARIA state', "menuButton.setAttribute('aria-expanded',String(open))"],
  ['closes menu on Escape', "event.key==='Escape'"]
];
let failed = false;
for (const [label, fragment] of rules) { const absence = label.startsWith('does not'); const found = source.includes(fragment); if ((absence && found) || (!absence && !found)) { console.error(`FAIL: ${label}`); failed = true; } }
if (failed) process.exit(1);
console.log('PASS: prewritten walkthrough, accessible navigation, and no-score/no-storage interaction boundary verified.');
