---
tags: 
  - noun
  - cultist_sim
---

<%*
let filename = tp.file.title
if ( filename.startsWith("Untitled") ) {
  filename = await tp.system.prompt("File name: ")
  await tp.file.rename(filename)
} 
tR += `# ${filename}`
%>

## Description

> <% tp.file.cursor() %><%* app.workspace.activeLeaf.view.editor?.focus(); %>

## Aspects
## Source

## Uses