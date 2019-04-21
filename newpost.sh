#!/usr/bin/env bash

cat >> draft-to-move.md <<EOF
---
date: $(date --utc +%FT%TZ)
title: Model
description:
---

# Model

[Instructions (includes part list)](model-instructions.pdf)

## Meta

* Time needed to digitalize: ~??? minutes
* Dimensions: ???x???x???cm, ???g, ??? parts, ??? distinct parts

EOF