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