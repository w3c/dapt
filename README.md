# dapt
The Dubbing and Audio description Profiles of TTML2, 
by the [Timed Text Working Group](https://www.w3.org/AudioVideo/TT/) 
is a profile of TTML2 suitable for the scripting, voicing and audio mixing 
of dubbing tracks and audio description for video.
This work was originally a combination of 
The [Audio Description Profile of TTML2](https://w3c.github.io/adpt/) 
, which was originally made by the [Audio Description Community Group](https://www.w3.org/community/audio-description/), 
and [Timed Text Authoring Lineage (TTAL)](https://netflixtechblog.com/introducing-netflix-timed-text-authoring-lineage-6fb57b72ad41). 

It is intended to meet the requirements set out in the 
[Requirements for Dubbing and Audio description](https://w3c.github.io/dapt-reqs/). 

The Editor's Draft can be viewed at https://w3c.github.io/dapt/

## Building

The specification is built using [Respec](https://respec.org/) and needs no
additional build steps for the main body. The figures are written in
[PlantUML](https://plantuml.com) and need to be exported in SVG format
after any changes.

### PlantUML Figures

The PlantUML figures' source files are in `/figures/sources`.

The PlantUML figures can be exported as SVG via the command line,
but IDE support in e.g. VSCode can make the editing experience simpler.

#### Using VSCode with PlantUML Extension

If using VSCode with the [PlantUML Extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), the following workspace settings may be helpful:

```json
{
    "plantuml.diagramsRoot": "figures/sources",
    "plantuml.exportFormat": "svg",
    "plantuml.exportOutDir": "figures",
    "plantuml.exportSubFolder": false,
}
```

Then while editing the source, running "PlantUML: Export Current Diagram"
from the command palette will regenerate the SVG and write the output to
the correct location, `/figures`.

### Tidying the SVG output for validation

Unfortunately the SVG that PlantUML generates from our source files has some structural issues that cause it to fail the W3C's HTML validator.
The following steps can be taken to fix them. It'd be neat to automate this somehow, one day...
1. delete `contentStyleType="text/css"`
2. delete text matching the regexp ` title="[#a-zA-Z\-]+"`
3. delete text matching the regexp = ` codeline="[#a-zA-Z0-9\-]+"`
4. deduplicate id values, e.g. id="link_Text_Style" in more than one place - a specific problem with the two links from Text to Style in the class diagram. E.g. change the "other" link with `id="link_Text_Style"` to `id="link_Text_Style_other"`
5. Move <a> wrappers from around boxes which contain other <a> elements, which therefore get nested, so the link is not on the box but is on the top text.
   * Specifically, where there is `/svg/a/g/text` move the `<a>` wrappers to being around the `<text>` that includes the text that's relevant.
   * It then becomes `/svg/g/a/text` (where the `a` has is the second child of the `g`, the first being a `rect`)
   * Atsushi also moved the `<rect>` at `/svg/a/g/rect` out of the `<g>` so there is `/svg/rect` followed by `/svg/g/a/text` but why? Seems okay without doing that.
