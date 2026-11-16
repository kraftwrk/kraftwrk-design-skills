// In-page measurements for audit.py. Two functions, each evaluated by the driver.
// Everything is read from the render (computed styles and boxes), never from the source.
({
  // Measurements for one screen root. args: {sel, key, skip}. Anything inside [data-system] (status bar, home indicator, system keyboard) is left out.
  screen: (args) => {
    const root = document.querySelector(args.sel);
    if (!root) return { missing: true };
    const out = { runs: [], blocks: [], spacing: {}, optical: {}, radii: {}, targets: [], names: [], levels: [], rhythm: [], cards: [], tells: [], clipped: [], truncated: 0, hiddenAtRest: [], eyebrows: [] };
    const num = (v) => { const n = parseFloat(v); return isNaN(n) ? 0 : n; };
    const cv = document.createElement('canvas'); cv.width = cv.height = 1;
    const cx = cv.getContext('2d', { willReadFrequently: true });
    const cache = new Map();
    const rgba = (c) => {
      if (cache.has(c)) return cache.get(c);
      cx.clearRect(0, 0, 1, 1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1);
      const d = cx.getImageData(0, 0, 1, 1).data; const o = { r: d[0], g: d[1], b: d[2], a: d[3] / 255 };
      cache.set(c, o); return o;
    };
    const over = (f, b) => ({ r: f.r * f.a + b.r * (1 - f.a), g: f.g * f.a + b.g * (1 - f.a), b: f.b * f.a + b.b * (1 - f.a), a: 1 });
    const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
    const contrast = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
    const dark = matchMedia('(prefers-color-scheme: dark)').matches && /dark/.test(getComputedStyle(document.documentElement).colorScheme);
    const bgOf = (el) => {
      const layers = []; let img = false, n = el;
      while (n && n.nodeType === 1) {
        const cs = getComputedStyle(n);
        if (cs.backgroundImage !== 'none') img = true;
        const c = rgba(cs.backgroundColor);
        if (c.a > 0) { layers.push(c); if (c.a >= 1) break; }
        n = n.parentElement;
      }
      let base = dark ? { r: 18, g: 18, b: 18, a: 1 } : { r: 255, g: 255, b: 255, a: 1 };
      for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base);
      return { c: base, img };
    };
    const SKIP = '[data-system]' + (args.skip ? ',' + args.skip : '');
    const hidden = (el) => {
      if (el.closest(SKIP)) return true;
      for (let n = el; n && n !== root.parentElement; n = n.parentElement) {
        const cs = getComputedStyle(n);
        if (cs.display === 'none' || cs.visibility === 'hidden' || (n !== root && n.hasAttribute('inert'))) return true;
      }
      return false;
    };
    const opacityOf = (el) => { let op = 1; for (let n = el; n && n !== root.parentElement; n = n.parentElement) op *= num(getComputedStyle(n).opacity); return op; };
    const label = (el) => el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
    const rr = root.getBoundingClientRect();
    const scale = root.offsetWidth ? rr.width / root.offsetWidth : 1;
    const px = (v) => Math.round((v / scale) * 10) / 10;

    // 1. Text runs: size, weight, family, leading, tracking, contrast.
    const paints = (m) => { if (m.matches('img,video,canvas,svg,picture')) return true; const cs = getComputedStyle(m); return cs.backgroundImage !== 'none' || rgba(cs.backgroundColor).a > 0.05; };
    const media = [...root.querySelectorAll('*')].filter((m) => !m.closest('svg svg, svg *') && paints(m)).map((m) => ({ m, r: m.getBoundingClientRect() })).filter((x) => x.r.width >= 24 * scale && x.r.height >= 24 * scale);
    const blocks = new Map();
    const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let t;
    while ((t = tw.nextNode())) {
      const s = t.nodeValue.replace(/\s+/g, ' ').trim(); if (!s) continue;
      const el = t.parentElement; if (!el || el.closest('svg,script,style,noscript,template')) continue;
      if (hidden(el)) continue;
      const rng = document.createRange(); rng.selectNodeContents(t);
      const rects = [...rng.getClientRects()].filter((r) => r.width > 0 && r.height > 0); if (!rects.length) continue;
      const cs = getComputedStyle(el), op = opacityOf(el);
      if (op < 0.02) { out.hiddenAtRest.push(s.slice(0, 40)); continue; }
      const fs = num(cs.fontSize), fw = parseInt(cs.fontWeight) || 400;
      const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
      const lh = cs.lineHeight === 'normal' ? null : num(cs.lineHeight);
      const ls = cs.letterSpacing === 'normal' ? 0 : num(cs.letterSpacing);
      const letters = s.replace(/[^\p{L}]/gu, '');
      const upper = cs.textTransform === 'uppercase' || (letters.length >= 3 && letters === letters.toUpperCase() && letters !== letters.toLowerCase());
      const fg = rgba(cs.color), bg = bgOf(el);
      const box = rects.reduce((a, r) => ({ l: Math.min(a.l, r.left), t: Math.min(a.t, r.top), r: Math.max(a.r, r.right), b: Math.max(a.b, r.bottom) }), { l: 1e9, t: 1e9, r: -1e9, b: -1e9 });
      const overMedia = media.some(({ m, r }) => !m.contains(el) && !el.contains(m) && Math.min(box.r, r.right) - Math.max(box.l, r.left) > (box.r - box.l) * 0.3 && Math.min(box.b, r.bottom) - Math.max(box.t, r.top) > (box.b - box.t) * 0.3);
      const fgc = over({ r: fg.r, g: fg.g, b: fg.b, a: fg.a * op }, bg.c);
      // text that starts on the screen and runs off its side, outside a sideways scroller
      // What an element of its own clips or scrolls (an ellipsis, a rail) is not counted: only what is left of the text after that.
      if (box.l < rr.right - 1 && box.r > rr.left + 1 && (box.r > rr.right + 1 || box.l < rr.left - 1) && !el.closest('[aria-hidden="true"]:not([inert])')) {
        let l = box.l, r = box.r;
        for (let n = el; n && n !== root; n = n.parentElement) { if (getComputedStyle(n).overflowX !== 'visible') { const q = n.getBoundingClientRect(); l = Math.max(l, q.left); r = Math.min(r, q.right); } }
        if (r > l && (r > rr.right + 1 || l < rr.left - 1)) out.clipped.push({ where: label(el), s: s.slice(0, 40), edge: true });
      }
      const run = { s: s.slice(0, 48), txt: s, code: !!el.closest('code,pre,kbd,samp'), dis: !!el.closest('[disabled],[aria-disabled="true"],[aria-busy="true"]'), it: cs.fontStyle === 'italic', n: s.length, fs, fw, fam, lh, ls: fs ? Math.round((ls / fs) * 1000) / 1000 : 0, upper, tag: el.tagName.toLowerCase(), where: label(el), col: [fg.r, fg.g, fg.b, +(fg.a * op).toFixed(2)], bg: [Math.round(bg.c.r), Math.round(bg.c.g), Math.round(bg.c.b)], ratio: +contrast(fgc, bg.c).toFixed(2), large: fs >= 24 || (fs >= 18.66 && fw >= 700), lines: 0 };
      let id = el.getAttribute('data-audit-id'); if (!id) { window.__auditUid = (window.__auditUid || 0) + 1; id = 'a' + window.__auditUid; el.setAttribute('data-audit-id', id); }
      run.id = id; run.over = bg.img || overMedia;
      out.runs.push(run);
      const blk = el.closest('p,li,dd,dt,blockquote,figcaption,h1,h2,h3,h4,h5,h6,[role=heading]');
      if (blk && root.contains(blk)) blocks.set(blk, (blocks.get(blk) || 0) + s.length + 1);
    }

    // 2. Blocks: lines, characters per line, last-line fill.
    for (const [blk, chars] of blocks) {
      const r = document.createRange(); r.selectNodeContents(blk);
      const rects = [...r.getClientRects()].filter((q) => q.width > 1).sort((a, b) => a.top - b.top || a.left - b.left);
      const lines = [];
      for (const q of rects) {
        const last = lines[lines.length - 1];
        if (last && q.top < last.b - q.height * 0.5) { last.l = Math.min(last.l, q.left); last.r = Math.max(last.r, q.right); last.b = Math.max(last.b, q.bottom); } else lines.push({ l: q.left, r: q.right, b: q.bottom });
      }
      if (!lines.length) continue;
      const widths = lines.map((l) => l.r - l.l), max = Math.max(...widths), fill = widths[widths.length - 1] / max;
      const cs = getComputedStyle(blk);
      out.blocks.push({ where: label(blk), heading: /^h[1-6]$/i.test(blk.tagName) || blk.getAttribute('role') === 'heading', chars, lines: lines.length, cpl: Math.round(chars / Math.max(1, lines.length - 1 + fill)), fill: +fill.toFixed(2), fs: num(cs.fontSize), lh: cs.lineHeight === 'normal' ? null : num(cs.lineHeight), wrap: cs.textWrapStyle || cs.textWrap || '', s: (blk.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40) });
    }

    // 3. Boxes: spacing on the grid, radii, separation, tells.
    const bump = (o, k, eg) => { (o[k] = o[k] || { n: 0, eg }).n++; };
    const SP = ['margin-top', 'margin-right', 'margin-bottom', 'margin-left', 'padding-top', 'padding-right', 'padding-bottom', 'padding-left', 'row-gap', 'column-gap'];
    const shadows = (v) => v.split(/,(?![^(]*\))/).map((p) => { const m = p.match(/(rgba?\([^)]+\)|#[0-9a-f]+|[a-z]+\([^)]+\))/i); const nums = p.replace(/(rgba?\([^)]+\)|[a-z]+\([^)]+\))/gi, '').match(/-?[\d.]+px/g) || []; return { c: m ? rgba(m[1]) : { r: 0, g: 0, b: 0, a: 0 }, x: num(nums[0]), y: num(nums[1]), blur: num(nums[2]), inset: /inset/.test(p) }; });
    const isControl = (el) => el.matches('button,a,input,select,textarea,label,summary,[role=button],[role=tab],[role=switch],[role=checkbox],[role=radio]');
    const cardSet = new Set();
    const rootArea = rr.width * rr.height;
    root.querySelectorAll('*').forEach((el) => {
      if (el.closest('svg') || hidden(el)) return;
      const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
      const cs = getComputedStyle(el), sm = el.computedStyleMap ? el.computedStyleMap() : null;
      if (sm) for (const p of SP) { const v = sm.get(p); if (!v || v.unit !== 'px' || !v.value) continue; const a = Math.abs(v.value); if (a < 4) bump(out.optical, v.value, p + ' on ' + label(el)); else if (Math.abs(a / 4 - Math.round(a / 4)) > 0.01) bump(out.spacing, Math.round(v.value * 100) / 100, p + ' on ' + label(el)); }
      const rad = num(cs.borderTopLeftRadius);
      if (rad > 0 && !/%/.test(cs.borderTopLeftRadius) && rad < Math.min(el.offsetWidth, el.offsetHeight) / 2 - 0.5) bump(out.radii, rad, label(el));
      const sides = ['Top', 'Right', 'Bottom', 'Left'];
      const bw = sides.map((s) => (cs['border' + s + 'Style'] !== 'none' && rgba(cs['border' + s + 'Color']).a > 0.05 ? num(cs['border' + s + 'Width']) : 0));
      const edges = bw.filter((w) => w > 0).length;
      for (const i of [1, 3]) if (bw[i] >= 2 && bw[i] > Math.max(bw[0], bw[2]) && bw[i] !== bw[i === 1 ? 3 : 1]) out.tells.push({ id: 'side-stripe', where: label(el), v: bw[i] + 'px ' + sides[i].toLowerCase() + ' border' });
      const sh = cs.boxShadow !== 'none' ? shadows(cs.boxShadow) : [];
      const outer = sh.filter((s) => !s.inset && s.c.a > 0.03);
      const own = rgba(cs.backgroundColor), parentBg = el.parentElement ? bgOf(el.parentElement).c : { r: 255, g: 255, b: 255 };
      const tinted = own.a > 0.05 && Math.abs(over(own, parentBg).r - parentBg.r) + Math.abs(over(own, parentBg).g - parentBg.g) + Math.abs(over(own, parentBg).b - parentBg.b) > 6;
      if (edges >= 3 && outer.length && tinted) out.tells.push({ id: 'border-shadow-tint', where: label(el), v: 'border, shadow and tint on one element' });
      for (const s of outer) {
        const spread = Math.max(s.c.r, s.c.g, s.c.b) - Math.min(s.c.r, s.c.g, s.c.b);
        if (s.x === 0 && s.y === 0 && s.blur > 0 && spread >= 40 && s.c.a >= 0.15) out.tells.push({ id: 'glow', where: label(el), v: cs.boxShadow.slice(0, 60) });
        if (s.blur === 0 && Math.max(Math.abs(s.x), Math.abs(s.y)) >= 4) out.tells.push({ id: 'hard-shadow', where: label(el), v: cs.boxShadow.slice(0, 60) });
      }
      if (cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text') out.tells.push({ id: 'gradient-text', where: label(el), v: 'background clipped to text' });
      if (/repeating-(linear|conic|radial)-gradient/.test(cs.backgroundImage)) out.tells.push({ id: 'stripes', where: label(el), v: 'repeating gradient' });
      const pad = num(cs.paddingTop) + num(cs.paddingBottom) + num(cs.paddingLeft) + num(cs.paddingRight);
      if ((tinted || edges >= 3 || outer.length) && !isControl(el) && !el.closest('button,a,label') && r.width >= 96 * scale && r.height >= 56 * scale && pad >= 16 && r.width * r.height < rootArea * 0.85 && el.textContent.trim()) cardSet.add(el);
      const clip = /hidden|clip/.test(cs.overflowX + cs.overflowY);
      const ownText = [...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim());
      if (clip && ownText && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1)) {
        if (cs.textOverflow === 'ellipsis' || (cs.webkitLineClamp && cs.webkitLineClamp !== 'none')) out.truncated++; else out.clipped.push({ where: label(el), s: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40) });
      }
    });
    for (const el of cardSet) { let p = el.parentElement; while (p && p !== root) { if (cardSet.has(p)) { out.cards.push({ where: label(el), inside: label(p) }); break; } p = p.parentElement; } }

    // 4. Hit targets and accessible names.
    const INTER = 'a[href],button,input:not([type=hidden]),select,textarea,summary,[role=button],[role=tab],[role=switch],[role=link],[role=checkbox],[role=radio],[role=menuitem]';
    root.querySelectorAll(INTER).forEach((el) => {
      if (hidden(el)) return;
      const cs = getComputedStyle(el);
      const host = el.matches('input,select,textarea,[role=switch],[role=checkbox],[role=radio]') ? el.closest('label') || (el.matches('input[type=checkbox],input[type=radio]') && el.id && root.querySelector('label[for="' + el.id + '"]')) || el : el;
      let l = 0, tt = 0, r = host.offsetWidth, b = host.offsetHeight;
      if (host === el) for (const ps of ['::before', '::after']) {
        const p = getComputedStyle(el, ps); if (p.content === 'none' || p.position !== 'absolute') continue;
        l = Math.min(l, num(p.left)); r = Math.max(r, el.offsetWidth - num(p.right)); tt = Math.min(tt, num(p.top)); b = Math.max(b, el.offsetHeight - num(p.bottom));
      }
      const inlineText = cs.display === 'inline' && el.parentElement && el.parentElement.textContent.trim().length - el.textContent.trim().length >= 20;
      const name = (el.getAttribute('aria-label') || (el.getAttribute('aria-labelledby') ? 'x' : '') || el.getAttribute('title') || (el.innerText || '').replace(/\s+/g, ' ').trim() || (el.querySelector('img[alt]:not([alt=""]), [role=img][aria-label], svg[aria-label]') ? 'x' : '') || (el.querySelector('svg title') ? 'x' : '') || el.getAttribute('value') || '').trim();
      const field = el.matches('input:not([type=submit]):not([type=button]),select,textarea');
      const labelled = !field || el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.closest('label') || (el.id && document.querySelector('label[for="' + el.id + '"]'));
      if (!field && !name) out.names.push({ where: label(el), v: 'no accessible name' });
      if (field && !labelled) out.names.push({ where: label(el), v: el.getAttribute('placeholder') ? 'placeholder as the only label' : 'field without a label' });
      out.targets.push({ where: label(el), name: (name || '').slice(0, 28), w: Math.round(r - l), h: Math.round(b - tt), inlineText, text: !!(el.innerText || '').trim() });
    });
    root.querySelectorAll('img').forEach((el) => { if (!hidden(el) && !el.hasAttribute('alt')) out.names.push({ where: label(el), v: 'image without alt' }); });

    // 5. Headings: order and rhythm (space above against space below).
    root.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach((h) => {
      if (hidden(h)) return;
      out.levels.push(+h.tagName[1]);
      const vis = (n, dir) => { while (n && (hidden(n) || !n.getBoundingClientRect().height || getComputedStyle(n).position === 'absolute')) n = n[dir]; return n; };
      const prev = vis(h.previousElementSibling, 'previousElementSibling'), next = vis(h.nextElementSibling, 'nextElementSibling');
      if (!prev || !next) return;
      const hr = h.getBoundingClientRect(), above = px(hr.top - prev.getBoundingClientRect().bottom), below = px(next.getBoundingClientRect().top - hr.bottom);
      const pcs = getComputedStyle(prev), pt = (prev.innerText || '').replace(/\s+/g, ' ').trim();
      const eyebrow = pt.length > 0 && pt.length <= 48 && !prev.querySelector('h1,h2,h3,h4,h5,h6,img,svg,button') && num(pcs.fontSize) <= Math.max(14, Math.min(16, num(getComputedStyle(h).fontSize) * 0.45));
      if (eyebrow) { const pl = pt.replace(/[^\p{L}]/gu, ''); out.eyebrows.push({ where: label(prev), s: pt.slice(0, 40), over: (h.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 32), caps: pcs.textTransform === 'uppercase' || (pl.length >= 3 && pl === pl.toUpperCase()) }); return; }
      if (above >= 0 && below > 0) out.rhythm.push({ where: label(h), s: (h.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 32), above, below });
    });
    return out;
  },

  // Page-wide scan of the stylesheets and the parts the browser draws.
  page: () => {
    const res = { transitions: [], animations: [], keyframes: {}, reduced: false, hover: 0, hoverGuarded: 0, hoverSelf: [], selection: false, focusVisible: false, blocked: 0 };
    const root = document.documentElement, rcs = getComputedStyle(root);
    res.colorScheme = rcs.colorScheme; res.accent = rcs.getPropertyValue('--accent').trim();
    const walk = (rules, ctx) => {
      for (const r of rules) {
        const cond = r.conditionText || (r.media && r.media.mediaText) || '';
        if (r.type === 4) { const red = /prefers-reduced-motion/.test(cond); if (red) res.reduced = true; walk(r.cssRules, { reduced: ctx.reduced || red, hover: ctx.hover || /hover:\s*hover/.test(cond) }); }
        else if (r.type === 7) { const props = new Set(); for (const k of r.cssRules) for (const p of k.style) props.add(p); res.keyframes[r.name] = [...props]; }
        else if (r.type === 1) {
          const sel = r.selectorText || '', st = r.style;
          if (/::selection/.test(sel)) res.selection = true;
          if (/:focus-visible/.test(sel)) res.focusVisible = true;
          if (/:hover/.test(sel)) { res.hover++; if (ctx.hover) res.hoverGuarded++; if (st.transform && /:hover\s*(,|$)/.test(sel)) res.hoverSelf.push(sel.slice(0, 70)); }
          if (!ctx.reduced && st.animationName && st.animationName !== 'none') res.animations.push({ where: sel.slice(0, 70), name: st.animationName, dur: st.animationDuration, ease: st.animationTimingFunction, iter: st.animationIterationCount });
          if (r.cssRules && r.cssRules.length) walk(r.cssRules, ctx);
        } else if (r.cssRules) walk(r.cssRules, ctx);
      }
    };
    for (const sh of document.styleSheets) { try { walk(sh.cssRules, { reduced: false, hover: false }); } catch (e) { res.blocked++; } }
    const seen = new Set();
    document.querySelectorAll('*').forEach((el) => {
      const cs = getComputedStyle(el);
      if (cs.transitionDuration.split(',').every((d) => parseFloat(d) === 0)) return;
      const key = cs.transitionProperty + '|' + cs.transitionDuration + '|' + cs.transitionTimingFunction;
      if (seen.has(key)) return; seen.add(key);
      res.transitions.push({ where: el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/)[0] : ''), prop: cs.transitionProperty, dur: cs.transitionDuration, ease: cs.transitionTimingFunction });
    });
    const input = document.querySelector('input:not([type=hidden]),textarea'), toggle = document.querySelector('input[type=checkbox],input[type=radio],input[type=range],progress');
    res.caret = input ? getComputedStyle(input).caretColor !== getComputedStyle(input).color && getComputedStyle(input).caretColor !== 'auto' : null;
    res.accentColor = toggle ? getComputedStyle(toggle).accentColor !== 'auto' : null;
    const ul = [...document.querySelectorAll('a')].find((a) => /underline/.test(getComputedStyle(a).textDecorationLine));
    res.underlineOffset = ul ? getComputedStyle(ul).textUnderlineOffset !== 'auto' : null;
    res.lang = root.getAttribute('lang') || '';
    return res;
  },
})
