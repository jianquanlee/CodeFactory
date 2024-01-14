#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# 持续进行Git Clone，直到成功
while ! git clone https://github.com/hpcaitech/ColossalAI.git; do echo "Cloning failed, retrying..."; sleep 2; done
