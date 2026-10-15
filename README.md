### Hi, I'm Filip 👋

My to-build list is longer than my free time, but a few things have made it out the door. 

📫 [contact@bosknumis.me](mailto:contact@bosknumis.me) · 🌐 [bosknumis.me](https://bosknumis.me) · 🐕 [fetchound.app](https://fetchound.app) · 🐈‍⬛ [littletangent.tech](https://littletangent.tech)

#### 🔎 Things I've built

- **[market-surveillance-toolkit](https://github.com/Bosk00/market-surveillance-toolkit)**: real-time order-book anomaly detection, entity-level wallet monitoring, and an ML risk-scoring model, backed by independent audit and validation pipelines.
- **[hibid-auction-watcher](https://github.com/Bosk00/hibid-auction-watcher)**: a self-hosted FastAPI app that scores and ranks auction listings per person, with a learned-feedback layer on top of the rule-based scoring.

#### 🧰 Currently tinkering with

- **[Shop Sketch](https://bosknumis.me/workshop)**: a browser-based woodworking planner. Build in an interactive 3D view (or switch to front, top, and side), start from bookshelf, table, or workbench templates, and select multiple boards to move, copy, and paste whole sections at once. Every part in the cut list is labeled by lumber type (1×4, 2×4, 1×12, plywood) and rolls up into a shopping list that tells you how many boards and sheets to actually buy, with a cut plan that packs parts onto stock boards and plywood sheets. Export the cut list as CSV, or download a labeled SVG of any single view, an isometric drawing, a parts diagram with each piece drawn at cut size, or everything on one sheet. iOS-only (for now) AR shows your design at true size in your space, and desktop users can beam it to their phone with a QR code (or copy a generated URL to send to your device). It all runs client-side, so nothing leaves your browser.
- **[Fetchound](https://fetchound.app)**: a public, multi-user rebuild of hibid-auction-watcher above. Same scoring and feedback idea, but hosted, with accounts and per-user search terms, pulling listings from HiBid and eBay. New matches are bundled into an email digest, so you don't have to keep checking the app. Now in alpha: it's live and working, but expect rough edges. Bug reports and feature requests are welcome.
- **[Little Tangent](https://littletangent.tech)**: a swipe-able reading feed of the best passages from public-domain books, built to feel like UberFacts or Reels without the brain rot. You see a hook, tap to keep reading, and the feed learns your taste from what you read, skip, and save. That learning runs entirely in the browser (hashed bag-of-words vectors plus online logistic regression), so there are no accounts, no tracking, and nothing leaves your device. A gentle stop card appears after 15 passages or a streak of fast skips, with options to shuffle the order or change topics. Passages come from a Python pipeline that pulls Project Gutenberg books and scores them with rules.
- **[Lantern Delve](https://bosknumis.me/lantern-delve)**: a procedurally generated dungeon climber you can leave running on a side monitor or take over and play at full attention. You wake at the bottom of a pit with a lantern and no memory, and every room hands you a Papers, Please-style report: read the chest tells, a creature's mood, or a stranger's guild seal, then stamp a decision (strike, sneak, approve, deny, climb, or retreat). If you don't act, an autopilot makes the call (Focus, Assist, or Away mode), and upgrades bought at camp make it smarter at reading moods, chests, and forged seals. Watch in a first-person raycast view or a top-down map. The light shifts from lantern-amber toward cold daylight the higher you climb, your best height hangs as a lantern on the wall, and earlier delvers leave their remains where they fell. There's no ending yet, and you're always trying to beat your last climb. Early prototype: a single HTML page of vanilla JavaScript and canvas, with saves kept in your browser and no backend.
- **[Papers Patriot](https://bosknumis.me/papers-patriot)**: A satirical, Papers, Please style browser game. You work Booth 7 at the Intake & Citizenship Examination office. Applicants walk up from the queue, slide papers under the glass, and a rulebook that changes every day tells you who is American. Every rule is nonsense on purpose. Early pre-alpha.
- **[Operation Cowboy](https://bosknumis.me/operation-cowboy)**: First-person desert embassy defense. Day: mine the outcrops, sell ore, wall the road, buy upgrades. Night: strangers walk toward the gate. Some are friends, some are not. You have a second to decide. Early pre-alpha.
- **[Dust Hollow](https://bosknumis.me/dust-hollow)**: First-person desert zombie survival game. Early pre-alpha.
- **[homelab](https://github.com/Bosk00/homelab)**: Docker Compose infrastructure for a household media and automation stack, with network isolation and least-privilege container config.

#### 🛠️ Tech

**Daily:** `Linux` · `Docker` · `Python` · `Local LLMs (gpt-oss-20b)` · `AI-assisted dev (Claude)`

**Used in this or that project:** `FastAPI` · `asyncio / aiohttp` · `websockets` · `REST API integration` · `SMTP` · `SQLite` · `PostgreSQL` · `Scrapy` · `Zyte` · `Heroku` · `Clerk` · `pandas` · `XGBoost / scikit-learn` · `SHAP` · `Streamlit` · `Jinja2` · `APScheduler` · `Vue 3` · `Three.js` · `Vite` · `PWA` · `GitHub Actions` · `HTML` · `CSS` · `JavaScript`

#### 🎲 Off the clock

- 🔭 Researching a numismatic article on Paeonian coinage
- 🌱 Learning ethical hacking (LinkedIn Learning)
- 🐴 Fun fact: "Filip" is the Slavic form of the Greek Philip, which means "friend of horses"

---

<!-- QUOTE:START -->
*“I’m not superstitious, but I am a little stitious.” — Michael Scott*
<!-- QUOTE:END -->
