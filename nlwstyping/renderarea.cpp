#include "renderarea.h"

Graph baseGraph()
{
    return Graph(std::vector<Vertex>{Vertex(0,nadicCircle(),0.0,0.0,0.0,{})});
}

RenderArea::RenderArea(QWidget *parent)
    : QWidget{parent}
{
    currentMode = Traverse;
    loadKeyBinds();
    current = baseGraph();
}
/*
 * Keyboard Input, ActionID -> Action
 * esc,0 -> Traverse Mode
 * e,1 -> Node Adjust Mode
 * r,2 -> Ravoz Mode
 * d,3 -> Dictionary Mode
 * esc,4 -> exit selection
 * i,5 -> up
 * j,6 -> left
 * k,7 -> down
 * l,8 -> right
 * u,9 -> CCW
 * v,10 -> CW
 * enter,11 -> next
 * n,12 -> new node
 */
void RenderArea::loadKeyBinds()
{
    keybinds = {
        {Qt::Key_Escape,0},
        {Qt::Key_E,1},
        {Qt::Key_R,2},
        {Qt::Key_D,3},
        {Qt::Key_Escape,4},
        {Qt::Key_I,5},
        {Qt::Key_J,6},
        {Qt::Key_K,7},
        {Qt::Key_L,8},
        {Qt::Key_U,9},
        {Qt::Key_V,10},
        {Qt::Key_Enter,11},
        {Qt::Key_N,12}
    };
}
const std::tuple<float,float> up(0,1);
const std::tuple<float,float> down(0,-1);
const std::tuple<float,float> right(1,0);
const std::tuple<float,float> left(-1,0);
float dotCartesian(std::tuple<float,float> v1, std::tuple<float,float> v2)
{
    return std::get<0>(v1)*std::get<0>(v2)+std::get<1>(v1)*std::get<1>(v2);
}
float dotCartPolar(std::tuple<float,float> cart, std::tuple<float,float> polar)
{
    return std::get<0>(cart)*std::get<0>(polar)*std::cos(std::get<1>(polar))+std::get<1>(cart)*std::get<0>(polar)*std::sin(std::get<1>(polar));
}
/*
 * Traverse Mode:
 * 1. render the (n) outgoing edges of selected node with an outline/color difference
 * 2. assign selection controls:
 *   a. if n <= 4, use dir_edge·dir_cardinal to assign highest scoring edge to the matching cardninal traverse button
 *   b. if n >= 4, assign cardinal directions as above, but use rotation keys to snap to next edge in that direction
 * 3. use jump key to move to next selected node
 * 4. pressing enter on a node enters Node Adjust Mode
 */
/*
 * Node Adjust Mode:
 * 1. allow directional inputs to move/rotate selected node
 * 2. using edge selection rules above, alter binding point angles & positions (cancel with ???)
 * 3. pressing enter with an edge selected creates a null node in that direction (allows for fine-tuning paths)
 * 4. holding shift and navigating will select many edges/nodes to do operations to (like grouping into a sub-graph)
 * 5. pressing enter with a node selected edits the glyph:
 *   a. move/rotate components with directional inputs
 *   b. have keys for each shape, build splines, etc.
 *   c. have key for binding points
 *   d. press enter to finalize the glyph
 *   e. press ctrl+enter to saves it in dictionary ordered by sizes of shapes, e.g. for UNLWS.communicate, it'd be triangle, then line
 */
/*
 * Ravoz Edit Mode:
 * 1. on selected node, accept typed input for glyph
 * 2. on selected node, accept keypress for adding new edges
 */
/*
 * Dictionary Edit Mode:
 * 1. open dropdown search menu from selected node location
 *   a. search will allow finding the glyph by eng gloss, ravoz gloss, shape, or id
 *   b. click or enter to select
 *   c. by default, add all binding points (or minimum required for variadic glyphs) without domains
 * 2. if legal, add new edges as with ravoz mode
 */
void RenderArea::keyPressEvent(QKeyEvent *event)
{
    int key = event->key();
    int action = this->keybinds[key];
    QString text = event->text();
    switch(this->currentMode){
        case Traverse:
            break;
        case Node:
            break;
        case Ravoz:
            break;
        case Dictionary:
            break;
    }
}
