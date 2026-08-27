# Identity, Footer, and Static Discovery Audit

**Scope:** Published Action Boundary Brief project site and the pending Virtualmase root-directory source.  
**Audit date:** 2026-08-27.  
**Scope boundary:** Static source and public response review only. No performance, traffic, rank, Search Console, DNS, analytics, or third-party social-platform claim is made here.

## Current condition

| Area | Action Boundary Brief | Virtualmase root directory | Finding |
|---|---|---|---|
| Page title, description, canonical, and robots meta | Present | Present in source | A useful baseline, but not a complete discovery system. |
| Open Graph representation | Present with SVG image | Present with SVG image | Replace social-preview references with exact 1200×630 PNG assets; retain SVG as source art. |
| Twitter/X metadata | Missing | Present | Add equivalent card metadata to the Action Boundary Brief. |
| Favicon | Existing line-heavy relay | Existing line-heavy route glyph | Replace both with high-contrast geometric marks designed to remain recognizable at 16–32 px; add PNG fallbacks and a web manifest. |
| Structured data | One `SoftwareSourceCode` object | One `WebSite` object | Add a small, accurate `WebPage`/`WebSite` graph that describes visible page content only; do not add unsupported rich-result types. |
| Crawl files | `robots.txt`, one-URL sitemap | `robots.txt`, one-URL sitemap | Correct for each single-page property. Remove meaningless `priority`/`changefreq` hints; use absolute canonical URLs only. |
| AI-facing route summary | Missing | `llms.txt` present | Add a short bounded `llms.txt` to the public skill. It is an orientation file, not an indexation control. |
| Footer | Four valuable links but no grouped reader task, release status, or method trail | Three link groups but low visual hierarchy and no release/status reading path | Rebuild each footer as an operational continuation surface: **use**, **inspect**, **correct**, and **related property** routes, plus a clear current boundary. |
| Root availability | Not applicable | Source exists locally; root property has not been published | Do not claim the root directory is live until its owner-approved release occurs. |

## Improvement specification

### 1. Identity system

The **Action Boundary Brief** mark becomes a filled cobalt square containing a white relay path interrupted by a rust pause point. The **Virtualmase** mark becomes an atlas tile: a cobalt diagonal route crossing a paper field, anchored by a rust reference point. Both are functional symbols without text; their paired wordmarks remain live HTML for clarity and accessibility.

Each property receives an SVG source, 48×48 PNG fallback, 180×180 touch icon, 192×192 and 512×512 manifest icons, and a 1200×630 PNG social preview. The intentionally high-contrast marks serve their specific properties without pretending they are one global logo.

### 2. Footer as an operating layer

Each footer will answer four reader questions: **Use the work**; **inspect the evidence**; **raise a correction or concern**; and **continue to an independent related property**. A small release/status field will identify the property’s actual state and prevent source-ready work from being confused with a deployed service.

### 3. Static discovery controls

The public skill will receive accurate title and social metadata, a matching `WebSite`/`WebPage`/`SoftwareSourceCode` JSON-LD graph, a web manifest, exact image references, a short `llms.txt`, and lean crawl files. The root directory source receives the matching identity and discovery assets, a refined `WebSite` graph, and a release-status-aware footer.

No change will promise rankings, create a cross-domain canonical, submit a sitemap, modify Search Console, activate analytics, add tracking scripts, or make a claim not visible and supportable on the page. Google describes sitemap submission as a hint rather than a guarantee, recommends crawlable links and people-first content, and advises that structured data reflect visible page content. [1] [2] [3]

## Icon-scale visual check

The revised Action Boundary Brief 48×48 icon renders as a strongly contrasting cobalt relay: white path segments establish the flow and a rust end gate signals interruption. The revised Virtualmase 48×48 icon renders as a cobalt atlas route ending at a rust reference point. Both retain a clear primary silhouette at favicon scale and remain property-distinct; they do not rely on tiny wordmark text.

## References

[1] [Google Search Essentials](https://developers.google.com/search/docs/essentials)  
[2] [Google: Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)  
[3] [Google: Introduction to structured data markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
