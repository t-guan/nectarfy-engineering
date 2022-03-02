
namespace BeehiveGasSensor
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.ArduinoPort = new System.IO.Ports.SerialPort(this.components);
            this.conbut = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // ArduinoPort
            // 
            this.ArduinoPort.Parity = System.IO.Ports.Parity.Even;
            // 
            // conbut
            // 
            this.conbut.Location = new System.Drawing.Point(49, 42);
            this.conbut.Name = "conbut";
            this.conbut.Size = new System.Drawing.Size(159, 52);
            this.conbut.TabIndex = 0;
            this.conbut.Text = "Connect";
            this.conbut.UseVisualStyleBackColor = true;
            this.conbut.MouseClick += new System.Windows.Forms.MouseEventHandler(this.conbut_MouseClick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1294, 880);
            this.Controls.Add(this.conbut);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.IO.Ports.SerialPort ArduinoPort;
        private System.Windows.Forms.Button conbut;
    }
}

