#!/usr/bin/env bash

cat >> draft-to-move.md <<EOF
---
date: $(date --utc +%FT%TZ)
title: Model
description:
---

[Instructions (includes part list)](model-instructions.pdf)

## Rendered images

## Features

## Meta

* Time needed to digitalize: ~??? minutes
* Dimensions: ???x???x???cm, ???g, ??? parts, ??? distinct parts

EOF
