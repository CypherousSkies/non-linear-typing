#ifndef GLYPH_H
#define GLYPH_H

#include <vector>
#include <QPainterPath>

class Glyph
{
public:
    QPainterPath rep;
    bool isNadic;
    void addBindingPoint();
    //in the form of relative x,y,v_x,v_y where (x,y) is relative position, and (v_x,v_y) is a directional vector of said binding point
    std::vector<std::tuple<float,float,float,float>> bindingpoints;
    Glyph(QPainterPath r); //TODO: glyph representation
    Glyph(QPainterPath r, std::function<std::tuple<float,float,float,float>(int)> addpoints);
private:
    std::function<std::tuple<float,float,float,float>(int)> addFunction;
};
const Glyph emptyGlyph();
const Glyph nadicCircle();

#endif // GLYPH_H
