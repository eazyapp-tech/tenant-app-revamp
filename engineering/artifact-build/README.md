# Building the TAR artifact pages

Turns a TAR markdown file into the published HTML page. One source, no second drawing to drift.

```bash
python3 build.py ../../TAR-08-structure-lock.md /tmp/structure-lock.html "The Structure Lock"
python3 build.py ../../TAR-09-open-door-structure-lock.md /tmp/open-door.html "The Open Door Structure Lock"
```

- ```mermaid fences pass through as `<pre class="mermaid">`, HTML-escaped, so the artifact renderer receives the `<br/>` tokens intact. Artifacts render Mermaid natively; do not load a library.
- The ASCII bar fence is replaced on the page by a hand-drawn SVG. It picks `bar-open.svg` when the fence contains "Find a home" and `bar.svg` otherwise. **That check is why TAR-09 does not show TAR-08's bar**; both fences contain "the one slot that changes", so keying on that alone was a real bug.
- `SP` at the top of build.py must point at the directory holding the two SVGs.
- The markdown keeps its ASCII bar, which is what GitHub and Obsidian show.
