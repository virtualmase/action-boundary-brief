import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(new URL('..', import.meta.url).pathname);
const files = ['index.html', 'styles.css', 'script.js', '404.html', 'favicon.svg', 'og-image.svg', 'robots.txt', 'sitemap.xml', '.nojekyll', 'SKILL.md', 'README.md', 'CONTRIBUTING.md', 'SECURITY.md', 'CITATION.cff', 'LICENSE', 'QA.md', 'templates/action-boundary-brief.md', 'references/source-notes.md', 'research/discovery.md', 'scripts/validate_boundary_brief.py'];
const required = [
  ['index.html', '<link rel="canonical" href="https://virtualmase.github.io/action-boundary-brief/">'],
  ['index.html', 'Action Boundary Brief'],
  ['index.html', 'SKILL.md'],
  ['index.html', 'https://www.nist.gov/itl/ai-risk-management-framework'],
  ['index.html', 'https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14'],
  ['index.html', 'https://owasp.org/www-project-top-10-for-large-language-model-applications/'],
  ['SKILL.md', 'Do not use it as a substitute'],
  ['README.md', '[Apache License 2.0](LICENSE)'],
  ['QA.md', 'Release QA — Action Boundary Brief'],
  ['templates/action-boundary-brief.md', '**Prohibited action:**'],
  ['references/source-notes.md', 'does not claim'],
  ['robots.txt', 'Sitemap: https://virtualmase.github.io/action-boundary-brief/sitemap.xml'],
  ['sitemap.xml', 'https://virtualmase.github.io/action-boundary-brief/']
];
const prohibited = [/\bfetch\s*\(/i, /XMLHttpRequest/i, /sendBeacon/i, /localStorage/i, /sessionStorage/i, /vite/i, /react/i, /tailwind/i, /certified/i, /compliant/i, /score your/i];
let failed = false;
for (const file of files) if (!existsSync(resolve(root, file))) { console.error(`FAIL: missing ${file}`); failed = true; }
for (const [file, fragment] of required) { const text = readFileSync(resolve(root, file), 'utf8'); if (!text.includes(fragment)) { console.error(`FAIL: ${file} missing ${fragment}`); failed = true; } }
for (const file of ['index.html', 'styles.css', 'script.js', '404.html']) { const text = readFileSync(resolve(root, file), 'utf8'); for (const pattern of prohibited) if (pattern.test(text)) { console.error(`FAIL: ${file} contains prohibited ${pattern}`); failed = true; } }
if (failed) process.exit(1);
console.log(`PASS: ${files.length} release files, source links, self-canonical metadata, boundary language, and no-network/no-storage rules verified.`);
