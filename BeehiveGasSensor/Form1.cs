using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;

namespace BeehiveGasSensor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            arduinoPort.BaudRate = 9600;
            arduinoPort.PortName = comText.Text;
        }
        private void conbut_MouseClick(object sender, MouseEventArgs e)
        {
            if (arduinoPort.IsOpen == false)
            {
                arduinoPort.Open();
                conBut.Text = "Disconnect";

            }
            else
            {
                arduinoPort.Close();
                conBut.Text = "Connect";

            }
        }
    }
}
