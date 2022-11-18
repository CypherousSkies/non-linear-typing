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
    QLabel *consonantLabel;
    QLabel *vowelLabel;
    QLabel *numConnectionsLabel;
    QLabel *connectionAngleLabel;
    QLabel *jumpToLabel;
    QLabel *bufferAngleLabel;
    QLabel *penWidthLabel;
    QLabel *penStyleLabel;
    QLabel *penCapLabel;
    QLabel *penJoinLabel;
    QLabel *brushStyleLabel;
    QLabel *otherOptionsLabel;
    QComboBox *consonantBox;
    QComboBox *vowelBox;
    QSpinBox *connectionsBox;
    QSpinBox *connectionAngleBox;
    QSpinBox *bufferAngleBox;
    QComboBox *jumpToBox;
    QPushButton *jumpButton;
    QComboBox *shapeComboBox;
    QSpinBox *penWidthSpinBox;
    QComboBox *penStyleComboBox;
    QComboBox *penCapComboBox;
    QComboBox *penJoinComboBox;
    QComboBox *brushStyleComboBox;
    QCheckBox *antialiasingCheckBox;
    QCheckBox *transformationsCheckBox;
public:
    explicit Window(QWidget *parent = nullptr);

signals:

};

#endif // WINDOW_H
