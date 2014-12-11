#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFont>
#include <QApplication>
#include <QMessageBox>
#include <QDebug>
#include <QFile>
#include <QTextStream>
#include <QList>
#include <QAbstractButton>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("Setup Window");
    QFont font = ui->label->font();
    font.setPointSize(11);
    ui->label->setText("Email id :");
    ui->label_2->setText("Cell phone no. :");
    ui->label->setFont(font);
    ui->label_2->setFont(font);
    font.setPointSize(12);
    ui->label_3->setText("How would you like to receive a message?");
    font.setItalic(true);
    ui->label_3->setFont(font);
    font.setItalic(false);
    font.setPointSize(11);
    ui->radioButton->setFont(font);
    ui->radioButton_2->setFont(font);
    ui->radioButton_3->setFont(font);
    ui->lineEdit->setText("sangpang20@gmail.com");
    ui->lineEdit_2->setText("5712652653");
    ui->lineEdit->setDisabled(true);
    ui->lineEdit_2->setDisabled(true);
    socket = new QTcpSocket(this);
    IP_Address = "127.0.0.1";
    port = 9000;
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

void MainWindow::on_pushButton_clicked()
{
    QMessageBox *box = new QMessageBox();
    QString at = "";
    for(int i = 0; i < ui->lineEdit->text().length(); i++){
        if(ui->lineEdit->text()[i] == '@'){
            at = ui->lineEdit->text()[i];
        }
    }

    // both
    if(ui->radioButton_3->isChecked()){
        qDebug() << "Both email and cell phone is are checked.";
        if(ui->lineEdit->text().length() >= 5 && at == "@"){
            if(ui->lineEdit_2->text().length() == 10){
                writeProgram(ui->lineEdit->text(), ui->lineEdit_2->text());
            }else{
                box->setText("Invalid cell phone number.");
                box->setWindowTitle("Error");
                box->setIcon(QMessageBox::Critical);
                box->show();
            }
        }else{
            box->setText("Invalid email address.");
            box->setWindowTitle("Error");
            box->setIcon(QMessageBox::Critical);
            box->show();
        }

    }else if(ui->radioButton->isChecked()){
        // email only
        if (ui->lineEdit->text().length() >= 5 && at == "@"){
            qDebug() << "Email is checked.";
            writeProgram(ui->lineEdit->text(), "phone");
        }else{
            box->setText("Invalid email address.");
            box->setWindowTitle("Error");
            box->setIcon(QMessageBox::Critical);
            box->show();
        }

    }else if(ui->radioButton_2->isChecked()){
        // cell phone only
        if(ui->lineEdit_2->text().length() == 10){
            qDebug() << "cell phone is checked";
            writeProgram("email", ui->lineEdit_2->text());
        }else{
            box->setText("Invalid cell phone number.");
            box->setWindowTitle("Error");
            box->setIcon(QMessageBox::Critical);
            box->show();
        }
   }
}


void MainWindow::writeProgram(QString email, QString phone)
{
    socket->connectToHost(IP_Address, port);
    if (phone == "phone"){
        email = "<<<" + email;
        socket->write(email.toUtf8());
        socket->waitForBytesWritten(200);
    }else if (email == "email"){
        phone = ">>>" + phone;
        socket->write(phone.toUtf8());
        socket->waitForBytesWritten(200);
    }else{
        QString message = "---" + email + "+" + phone;
        socket->write(message.toUtf8());
        socket->waitForBytesWritten(200);
    }
    socket->flush();
    socket->close();
    qDebug() << "Message delivered.";
    qDebug() << email << "  " << phone;
}

void MainWindow::on_pushButton_2_clicked()
{
    QApplication::exit(1);
}

void MainWindow::on_radioButton_2_clicked()
{
    ui->lineEdit->clear();
    ui->lineEdit_2->setEnabled(true);
    ui->lineEdit->setDisabled(true);
}

void MainWindow::on_radioButton_clicked()
{
    ui->lineEdit_2->clear();
    ui->lineEdit->setEnabled(true);
    ui->lineEdit_2->setDisabled(true);
}

void MainWindow::on_radioButton_3_clicked()
{
    ui->lineEdit->setEnabled(true);
    ui->lineEdit_2->setEnabled(true);
}
