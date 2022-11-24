#include "window.h"
#include "renderarea.h"

#include <QtWidgets>

Window::Window(QWidget *parent)
    : QWidget{parent}
{
    setWindowTitle(tr("NLWS Typing System"));

    renderArea = new RenderArea;
    QGridLayout *mainLayout = new QGridLayout;
    mainLayout->setColumnStretch(0,1);
    mainLayout->setColumnStretch(3,1);
    mainLayout->addWidget(renderArea,0,0,1,4);
    setLayout(mainLayout);

    penChanged();
    brushChanged();
}

void Window::penChanged()
{
}

void Window::brushChanged()
{
}
