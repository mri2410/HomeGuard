#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QKeyEvent>
#include <QMessageBox>
#include <QString>
#include <QString>
#include <QFont>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("HomeGuard");
    ui->label->setText("Welcome!");
    font = ui->label->font();
    font.setPointSize(85);
    font.setBold(true);
    font.setStyleHint(QFont::Times);
    ui->label->setFont(font);
    QString msgLine1 = "If you would like to send us a message, type it in the text box below.";
    QString msgLine2 = "\n                                   When finished press OK.";
    ui->label_2->setText(msgLine1 + msgLine2);
    font.setPointSize(12);
    font.setBold(true);
    font.setStyleHint(QFont::Times);
    ui->label_2->setFont(font);
    font.setBold(false);
    font.setPointSize(14);
    ui->plainTextEdit->setFont(font);
    ui->pushButton->setGeometry(910,540,81,31);
    ui->pushButton->setText("OK");
    ui->pushButton_2->setGeometry(790, 540, 81, 31);
    ui->pushButton_2->setText("Cancel");
    ui->pushButton_3->setGeometry(670, 540, 81, 31);
    ui->pushButton_3->setText("Clear");
    font.setPointSize(11);
    ui->pushButton->setFont(font);
    ui->pushButton_2->setFont(font);
    ui->pushButton_3->setFont(font);
    PreviousMessage = " ";

    IP_Address = "127.0.0.1";
    port = 9000;
    socket = new QTcpSocket(this);
    socket->connectToHost(IP_Address, port);
    if(socket->waitForConnected(200)){
        qDebug() << "connection successuful.";
    }else{
        qDebug() << "connection failed";
    }
    socket->close();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::sendMessage(QString message)
{
    message = "$$$" + message;
    socket->connectToHost(IP_Address, port);
    socket->write(message.toUtf8());
    socket->waitForBytesWritten(200);
    socket->flush();
    socket->close();
     qDebug() << "Message delivered.";
}

void MainWindow::on_pushButton_clicked()
{
    QString text = ui->plainTextEdit->toPlainText();
    qDebug() << text;
    //ui->plainTextEdit->clear();
    QMessageBox *box = new QMessageBox();
    box->setWindowTitle("OK");
    font.setPointSize(11);
    box->setFont(font);
    if (text.length() <= 1){
        box->setText("No message is received.");
        box->show();
    }else{
        if(text == PreviousMessage){
            box->setText("Would you like to resend the message?");
            box->addButton(QMessageBox::Yes);
            box->addButton(QMessageBox::No);
            int selection = box->exec();
            if (selection == QMessageBox::Yes){
                // send message
                sendMessage(text);
                qDebug() << "Message sent.";
            }else if (selection == QMessageBox::No){
                // no need to do anything
            }
        }else{
            box->setText("Your message is successfully received.");
            PreviousMessage = text;
            sendMessage(text);
            box->show();
        }
    }

}

void MainWindow::on_pushButton_2_clicked()
{
    ui->plainTextEdit->clear();
    QMessageBox *box = new QMessageBox();
    box->setWindowTitle("Cancel");
    font.setPointSize(11);
    box->setFont(font);
    box->setText("Message cancelled.");
    box->show();
}

void MainWindow::on_pushButton_3_clicked()
{
    ui->plainTextEdit->clear();
}
