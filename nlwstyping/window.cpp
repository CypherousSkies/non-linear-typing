#include "window.h"
#include "renderarea.h"

#include <QtWidgets>

Window::Window(QWidget *parent)
    : QWidget{parent}
{
    renderArea = new RenderArea;

    consonantLabel = new QLabel(tr("&Consonant:"));
    consonantLabel->setBuddy(consonantBox);

    consonantBox = new QComboBox;
    consonantBox->addItem(tr("null"));
    consonantBox->addItem(tr("m"));
    consonantBox->addItem(tr("n"));
    consonantBox->addItem(tr("ŋ"));
    consonantBox->addItem(tr("b"));
    consonantBox->addItem(tr("d"));
    consonantBox->addItem(tr("p"));
    consonantBox->addItem(tr("t"));
    consonantBox->addItem(tr("s"));
    consonantBox->addItem(tr("f"));
    consonantBox->addItem(tr("š"));
    consonantBox->addItem(tr("ž"));
    consonantBox->addItem(tr("v"));
    consonantBox->addItem(tr("z"));
    consonantBox->addItem(tr("r"));
    consonantBox->addItem(tr("l"));
    consonantBox->addItem(tr("ř"));
    consonantBox->addItem(tr("g"));
    consonantBox->addItem(tr("k"));
    consonantBox->addItem(tr("h"));
    consonantBox->addItem(tr("x"));

    vowelLabel = new QLabel(tr("&Vowel:"));
    vowelLabel->setBuddy(vowelBox);

    vowelBox = new QComboBox;
    vowelBox->addItem(tr("i"));
    vowelBox->addItem(tr("ī"));
    vowelBox->addItem(tr("í"));
    vowelBox->addItem(tr("ì*"));
    vowelBox->addItem(tr("ȧ"));
    vowelBox->addItem(tr("ā"));
    vowelBox->addItem(tr("á"));
    vowelBox->addItem(tr("à*"));
    vowelBox->addItem(tr("ȯ"));
    vowelBox->addItem(tr("ō"));
    vowelBox->addItem(tr("ó"));
    vowelBox->addItem(tr("ò*"));
}
