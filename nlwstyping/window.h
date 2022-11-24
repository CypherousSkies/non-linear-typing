#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

QT_BEGIN_NAMESPACE
class QCheckBox;
class QComboBox;
class QLabel;
class QSpinBox;
class QPushButton;
QT_END_NAMESPACE
class RenderArea;

class Window : public QWidget
{
    Q_OBJECT
private slots:
    void shapeChanged();
    void penChanged();
    void brushChanged();

private:
    RenderArea *renderArea;
    QCheckBox *antialiasingCheckBox;
    QCheckBox *transformationsCheckBox;
public:
    explicit Window(QWidget *parent = nullptr);

signals:

};

#endif // WINDOW_H
