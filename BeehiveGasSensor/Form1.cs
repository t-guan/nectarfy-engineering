using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections.Concurrent;
using System.IO.Ports;

namespace BeehiveGasSensor
{
    public partial class Form1 : Form
    {
        ConcurrentQueue<Int32> dataPacket = new ConcurrentQueue<Int32>();
        ConcurrentQueue<Int32> dataArray = new ConcurrentQueue<Int32>();

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            arduinoPort.BaudRate = 9600;
            arduinoPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);
            timer1.Interval = 1000;
            timer1.Enabled = true;

        }
        private void DataReceivedHandler(object sender, SerialDataReceivedEventArgs e)
        {
            int bytesToRead = arduinoPort.BytesToRead;
            while (bytesToRead != 0)
            {
                int newByte = arduinoPort.ReadByte();
                dataPacket.Enqueue(newByte);
                bytesToRead = arduinoPort.BytesToRead;
            }
        }
        private void conbut_MouseClick(object sender, MouseEventArgs e)
        {
 
            if (arduinoPort.IsOpen == false)
            {
                arduinoPort.PortName = comBox.Text;
                arduinoPort.Open();
                conBut.Text = "Disconnect";

            }
            else
            {
                arduinoPort.Close();
                conBut.Text = "Connect";

            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (arduinoPort.IsOpen)
            {
                while (dataPacket.TryDequeue(out int valfromq))
                {
                    dataBox.AppendText(valfromq.ToString() + ",");
                }
            }
        }
    }
}
