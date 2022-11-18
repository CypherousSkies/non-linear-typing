#include "graph.h"

Graph::Graph(std::vector<Vertex> v)
{
    v_ = v;
    current_id = v.size();
}
Graph::Graph()
{
    v_ = std::vector<Vertex>();
    current_id = 0;
}

Vertex Graph::addVertex(Glyph &g, std::set<int> a)
{
    this->current_id += 1;
    Vertex v = Vertex(this->current_id,g,0,0,0,a);
    this->v_.push_back(v);
    return v;
}

Vertex Graph::addVertex(Glyph &g, float x, float y, float theta, std::set<int> a)
{
    this->current_id += 1;
    Vertex v = Vertex(this->current_id,g,x,y,theta,a);
    this->v_.push_back(v);
    return v;
}

void Graph::addConnection(int id1, int id2)
{
    Vertex v1 = this->v_.at(id1);
    Vertex v2 = this->v_.at(id2);
    v1.adjacents.insert(v2.vertex_number);
    v2.adjacents.insert(v1.vertex_number);
}

void Graph::addConnection(Vertex &v1, Vertex &v2)
{
    v1.adjacents.insert(v2.vertex_number);
    v2.adjacents.insert(v1.vertex_number);
}

void Graph::removeVertex(int id)
{
    this->v_.erase(this->v_.begin()+id);
}

void Graph::removeVertex(Vertex &v)
{
    this->v_.erase(this->v_.begin()+v.vertex_number);
}

void Graph::prune()
{
    for(int i=0;i<this->v_.size();i++){
        //re-number all vertices (as some may have been removed)
        //remove null nodes which have exactly one adjacent
    }
}

bool Graph::isPlanar()
{
    int v = this->v_.size();
    int e = 0;
    for (int i=0;  i < v; i++){
        std::set<int> a = this->v_[i].adjacents;
        bool found = false;
        for (auto itr : a){
            if(this->v_[itr].adjacents.find(i)!=this->v_[itr].adjacents.end()){
                e+=0.5;
                found = true;
            }
        }
        if(!found) e+=1;
    }
    return 3*v-e>=6;
}
