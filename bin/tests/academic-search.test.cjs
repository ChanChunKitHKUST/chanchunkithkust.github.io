const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('assets/js/academic.js', 'utf8');
const item = (text, status) => ({hidden: false, querySelector: selector => selector === '[data-status]' ? {dataset: {status}} : {textContent: text}});
const entries = [item('XToM Chunkit Chan 2026', 'Published'), item('NegotiationToM Chunkit Chan 2024', 'Published'), item('MuSeToM Chunkit Chan 2026', 'Under review'), item('LLM-Hanabi Fangzhou Liang 2025', 'Preprint')];
const headings = entries.map(() => ({tagName: 'H2', hidden: false}));
const groups = entries.map((entry, i) => ({children: [entry], previousElementSibling: headings[i]}));
const listeners = {};
const search = {value: '', addEventListener: (event, fn) => listeners[event] = fn};
const status = {textContent: ''};
const statusFilter = {value: 'all', addEventListener: (event, fn) => listeners[event] = fn};
const controls = {hidden: true};
let print;
let printed = false;
const document = {
  querySelector: selector => ({
    '[data-publication-search]': search,
    '[data-search-status]': status,
    '[data-publication-status]': statusFilter,
    '[data-search-controls]': controls,
    '[data-print]': {addEventListener: (_, fn) => print = fn}
  })[selector] || null,
  querySelectorAll: selector => selector === '.bibliography > li' ? entries : groups
};
vm.runInNewContext(source, {document, window: {print: () => printed = true}});
assert.equal(controls.hidden, false);
assert.equal(status.textContent, '4 publications');
function query(value) {search.value = value; listeners.input();}
query('  XTOM ');
assert.deepEqual(entries.map(e => e.hidden), [false, true, true, true]);
assert.deepEqual(headings.map(e => e.hidden), [false, true, true, true]);
assert.equal(status.textContent, '1 publication found');
query('2024');
assert.deepEqual(entries.map(e => e.hidden), [true, false, true, true]);
query('liang');
assert.deepEqual(entries.map(e => e.hidden), [true, true, true, false]);
query('not a publication');
assert.ok(groups.every(g => g.hidden));
assert.match(status.textContent, /No matching publications/);
query('');
assert.ok(entries.every(e => !e.hidden));
assert.ok(groups.every(g => !g.hidden));
statusFilter.value = 'Under review'; listeners.change();
assert.deepEqual(entries.map(e => e.hidden), [true, true, false, true]);
query('XToM');
assert.ok(entries.every(e => e.hidden));
query('');
statusFilter.value = 'Published'; listeners.change();
assert.deepEqual(entries.map(e => e.hidden), [false, false, true, true]);
statusFilter.value = 'Preprint'; listeners.change();
assert.deepEqual(entries.map(e => e.hidden), [true, true, true, false]);
statusFilter.value = 'all'; listeners.change();
assert.ok(entries.every(e => !e.hidden));
print();
assert.equal(printed, true);
// The same script must be safe on the home page, which has neither widget.
vm.runInNewContext(source, {document: {querySelector: () => null}});
console.log('PASS: title/author/year search, case/whitespace handling, empty state, reset, group visibility, status filters, combined search/filter, print action, and pages without widgets.');
