#include "glyph.h"

Glyph::Glyph(QPainterPath r)
{
    rep = r;
    isNadic = false;
}
Glyph::Glyph(QPainterPath r, std::function<std::tuple<float,float,float,float>(int)> addpoints)
{
    rep = r;
    isNadic = true;
    addFunction = addpoints;
}
void Glyph::addBindingPoint()
{
    bindingpoints.push_back(addFunction(bindingpoints.size()));
}
/*
 * Binding Points along a unit circle:
 * i        = 0 1   2 3   4   5   6   7   8   9   10  11  12  13   14   15
 * theta/pi = 0 1/2 1 3/2 1/4 3/4 5/4 7/4 1/8 3/8 5/8 7/8 9/8 11/8 13/8 15/8
 */
std::tuple<float,float,float,float> circleBindingPoints(int i)
{
    if (i == 0){
        return std::tuple(1,0,1,0);
    }
    int n = std::max<int>(0,std::ceil(log(i)/log(2) -2));
    float angle;
    int j = i % 4*std::pow(2,n);
    //don't ask how I arrived at this formula, it was a lot of fiddling in desmos
    if (i<4) angle = M_PI*i/2;
    else angle = M_PI*(j/std::pow(2,n)+1/(2*std::pow(2,n))+2*(n-1));
    return {std::cos(angle),std::sin(angle),std::cos(angle),std::sin(angle)};
}
// include a glyph for resolving crossings, possibly as a null/default value which is distinguished from a dangling edge by number of connections
const Glyph emptyGlyph()
{
    QPainterPath r;
    return Glyph(r);
}
const Glyph nadicCircle()
{
    QPainterPath r;
    r.addEllipse(QRectF(-1,-1,2,2));
    return Glyph(r, &circleBindingPoints);
}
