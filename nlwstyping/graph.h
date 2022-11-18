#ifndef GRAPH_H
#define GRAPH_H

#include <set>
#include <vector>
#include <glyph.h>

struct Vertex
{
    Vertex(int v, Glyph g, float x, float y, float t, std::set<int> a) : vertex_number(v), glyph(g), x(x), y(y), theta(t), adjacents(a) {}
    int vertex_number;
    Glyph glyph;
    int x;
    int y;
    int theta;
    std::set<int> adjacents;
};

class Graph
{
public:
    Graph(std::vector<Vertex> v);
    Graph();
    std::vector<Vertex> v_;
    Vertex addVertex(Glyph &g, std::set<int> a);
    Vertex addVertex(Glyph &g, float x, float y, float theta, std::set<int> a);
    void addConnection(int id1, int id2);
    void addConnection(Vertex &v1, Vertex &v2);
    void removeVertex(int id);
    void removeVertex(Vertex &v);
    void prune(); //re-numbers all vertices & connections
    bool isPlanar();
private:
    int current_id;
};

#endif // GRAPH_H
