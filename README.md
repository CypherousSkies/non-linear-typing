# non-linear-typing
This will be a text editor for [Ravoz](https://github.com/CypherousSkies/Ravoz/), [UNLWS](https://s.ai/nlws), and [Ouwi](https://ouwi.org/index.html); although it should, in principal, be able to be used for any non-linear writing system. I'll be using Qt for this because it's open source and has all the things I could ever need to make this work.

## Modes
Taking inspiration from `vim`, the editor will have a variety of "modes" while writing to better reflect the variety of ways writing might come to be:

### Traverse Mode
1. render the (n) outgoing edges of selected node with an outline/color difference
2. assign selection controls:
    a. if n <= 4, use dir_edge·dir_cardinal to assign highest scoring edge to the matching cardninal traverse button
    b. if n >= 4, assign cardinal directions as above, but use rotation keys to snap to next edge in that direction
 3. use jump key to move to next selected node
 4. pressing enter on a node enters Node Adjust Mode
 
### Node Adjust Mode
 1. allow directional inputs to move/rotate selected node
 2. using edge selection rules above, alter binding point angles & positions (cancel with ???)
 3. pressing enter with an edge selected creates a null node in that direction (allows for fine-tuning paths)
 4. holding shift and navigating will select many edges/nodes to do operations to (like grouping into a sub-graph)
 5. pressing enter with a node selected edits the glyph:
    a. move/rotate components with directional inputs
    b. have keys for each shape, build splines, etc.
    c. have key for binding points
    d. press enter to finalize the glyph
    e. press ctrl+enter to saves it in dictionary ordered by sizes of shapes, e.g. for UNLWS.communicate, it'd be triangle, then line

### Ravoz Edit Mode
 1. on selected node, accept typed input for glyph
 2. on selected node, accept keypress for adding new edges
 
### Dictionary Edit Mode
 1. open dropdown search menu from selected node location
    a. search will allow finding the glyph by eng gloss, ravoz gloss, shape, or id
    b. click or enter to select
    c. by default, add all binding points (or minimum required for variadic glyphs) without domains
 2. if legal, add new edges as with ravoz mode
 
## Under the Hood
The way I'm planning on making this work is by storing a work as a Graph with Glyphs for nodes and connections for edges. For the purposes of rendering, glyphs will encode SVG, position, and connection tangent (e.g. a vector originating at a binding point pointing in the direction to make the connection smooth) information.
Eventually I'll work towards being compatible with Graphviz's DOT language, but that's a long ways off.
