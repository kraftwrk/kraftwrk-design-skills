---
version: alpha
name: <product name>
description: <the brand idea in one sentence>
colors:
  canvas: "#FFFFFF"
  surface: "#F4F4F2"
  fg-primary: "#15171A"
  fg-secondary: "#5A6068"
  border-subtle: "#E3E5E8"
  border-strong: "#8A9099"
  accent: "#1F5FFF"
  on-accent: "#FFFFFF"
  danger: "#C62828"
typography:
  display:
    fontFamily: "<display face>, <metric-matched fallback>"
    fontSize: "2.25rem"
    fontWeight: 600
    lineHeight: "2.75rem"
    letterSpacing: "-0.02em"
  title:
    fontFamily: "<workhorse face>, <fallback>"
    fontSize: "1.375rem"
    fontWeight: 600
    lineHeight: "1.75rem"
    letterSpacing: "0em"
  body:
    fontFamily: "<workhorse face>, <fallback>"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: "1.5rem"
    letterSpacing: "0em"
  label:
    fontFamily: "<workhorse face>, <fallback>"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: "1.25rem"
    letterSpacing: "0em"
rounded:
  control: "8px"
  container: "16px"
  full: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.control}"
    height: "48px"
motion:
  press: "scale 0.97, 120ms, ease-out"
  sheet: "translate, 350ms, platform spring"
---

<!-- Every value above is a placeholder: replace it with the product's tokens. The motion group is this studio's addition to the format. -->

## Overview

The brand idea. The three attributes and their tension. The one or two carriers pushed to an extreme. The convention broken on purpose. The brand device and its named places.

## Colors

The canvas and its reason (the scene of use). The accent economy: where the accent appears and where it never does. The dark theme. On-image and inverse colours. Semantic colours.

## Typography

The type voice. Each face with its reason, and the licensed face a stand-in replaces. The scale steps in use per surface. The hero figure. Case and tracking.

## Layout

Grid, density, separation method, alignment edges, reading column.

## Elevation & Depth

The one elevation system.

## Shapes

Radius logic per tier. Icon family and stroke.

## Components

Navigation and action chrome. The patterns in use. States.

## Do's and Don'ts

The brand moments map (loud, medium, quiet). Imagery role and art direction. The motion signature. Voice. Exceptions to Material 3 and Apple HIG, each with its reason.
