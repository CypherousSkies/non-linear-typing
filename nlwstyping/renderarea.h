#ifndef RENDERAREA_H
#define RENDERAREA_H

#include <QBrush>
#include <QPen>
#include <QPixmap>
#include <QWidget>
#include <QPainterPath>
#include <QKeyEvent>
#include <QMenuBar>
#include <graph.h>

enum Mode { Traverse, Node, Ravoz, Dictionary };

class RenderArea : public QWidget
{
    Q_OBJECT
public:
    QSize minimumSizeHint() const override;
    QSize sizeHint() const override;
    Mode currentMode;
    void loadKeyBinds();
    Graph current;
    explicit RenderArea(QWidget *parent = nullptr);
public slots:
    void setPen(const QPen &pen);
    void setBrush(const QBrush &brush);
    void setAntialiased(bool antialiased);
    void update();
protected:
    void paintEvent(QPaintEvent *event) override;
    void keyPressEvent(QKeyEvent *event) override;
private:
    QPen pen;
    QBrush brush;
    bool antialiased;
    bool transformed;
    QPixmap pixmap;
    QMenuBar menu;
    std::map<int,int> keybinds;    
signals:

};

#endif // RENDERAREA_H
