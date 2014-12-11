#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtNetwork/QTcpSocket>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    
private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_radioButton_2_clicked();

    void on_radioButton_clicked();

    void on_radioButton_3_clicked();

private:
    Ui::MainWindow *ui;
    void writeProgram(QString, QString);
    QList <QString> lines;
    QTcpSocket *socket;
    QString IP_Address;
    int port;
};

#endif // MAINWINDOW_H
