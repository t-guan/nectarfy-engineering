
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
            this.arduinoPort = new System.IO.Ports.SerialPort(this.components);
            this.conBut = new System.Windows.Forms.Button();
            this.comText = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // arduinoPort
            // 
            this.arduinoPort.Parity = System.IO.Ports.Parity.Even;
            // 
            // conBut
            // 
            this.conBut.Location = new System.Drawing.Point(49, 42);
            this.conBut.Name = "conBut";
            this.conBut.Size = new System.Drawing.Size(159, 52);
            this.conBut.TabIndex = 0;
            this.conBut.Text = "Connect";
            this.conBut.UseVisualStyleBackColor = true;
            this.conBut.MouseClick += new System.Windows.Forms.MouseEventHandler(this.conbut_MouseClick);
            // 
            // comText
            // 
            this.comText.Location = new System.Drawing.Point(49, 113);
            this.comText.Name = "comText";
            this.comText.Size = new System.Drawing.Size(159, 31);
            this.comText.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1294, 880);
            this.Controls.Add(this.comText);
            this.Controls.Add(this.conBut);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.IO.Ports.SerialPort arduinoPort;
        private System.Windows.Forms.Button conBut;
        private System.Windows.Forms.TextBox comText;
    }
}

