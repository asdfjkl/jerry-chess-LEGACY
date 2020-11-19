# Jerry - Das Schachprogramm

![alt text](https://raw.githubusercontent.com/asdfjkl/jerry/master/jerryfx.png)

## About
Jerry is a cross-platform chess graphical user interface.

* based around one of the world's best chess program Stockfish
* play against the computer
* adjust strength levels to match your skill
* enter, edit and analyse games
* fully automatic game analysis
* read and save games in standard PGN format
* copy and paste FEN positions and pgn games from clipboard
* cross-platform: modern look on Linux and Windows
* handle large (i.e. 1 GB) PGN files
* easy and intuitive GUI
* free software (GNU GPL 2), no adware/spyware

## Download

Current Version: 4.0.0

* [Windows](https://github.com/asdfjkl/jerry/releases/tag/v4.0.0)
* Linux
  - install from [Snapstore](https://snapcraft.io/jerry) 
  - or install [manually](https://github.com/asdfjkl/jerry/releases/tag/v4.0.0)

## Changelog

Version 4.0.0 (Oct 2020)
 * complete rewrite
 * position search even in very large PGN files

Version 3.2.1 (Dec 2019)
 * bug fix in displaying move and position annotations
 * ability to flip board when entering a new position

Version 3.2.0 (July 2019)
 * MultiPV up to 4 lines
 * ability to handle and search (metadata) of large (> 1 GB) PGN files
 * user defined font-sizes
 
 ## Roadmap
 
Current plans for future versions:
 
Version 4.1
- bugfixes
- database: edit & save for large PGNs
- [done] colorize last move
- [done] drawing arrows & colorizing fields
- [done] keyboard shortcuts
- [done] Fullscreen mode

Version 4.2
- opening book support
- visual representation (i.e. graph) of game progress
- ability to set default database
- ship a default database of a few thousand interesting games 
- option to show arrow that illustrates engine top-move in analysis
- "drag" pieces in enter-position dialog
- show more engine info: Tablebase Hits and Hash percentage
- ship with pre-configured 4-piece (size!) tablebases
- ability to click on engine lines 
