namespace DllCompare
{
    partial class Main
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Main));
            this.btnOpenFolderA = new System.Windows.Forms.Button();
            this.txtFolderA = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBoxFolders = new System.Windows.Forms.GroupBox();
            this.checkColours = new System.Windows.Forms.CheckBox();
            this.checkHide = new System.Windows.Forms.CheckBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnOpenFolderB = new System.Windows.Forms.Button();
            this.txtFolderB = new System.Windows.Forms.TextBox();
            this.gridDllCompare = new System.Windows.Forms.DataGridView();
            this.btnRefresh = new System.Windows.Forms.Button();
            this.radioAssembly = new System.Windows.Forms.RadioButton();
            this.radioCreationTime = new System.Windows.Forms.RadioButton();
            this.colDll = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colFolderA = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.colFolderB = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.groupBoxFolders.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.gridDllCompare)).BeginInit();
            this.SuspendLayout();
            // 
            // btnOpenFolderA
            // 
            this.btnOpenFolderA.Location = new System.Drawing.Point(597, 29);
            this.btnOpenFolderA.Margin = new System.Windows.Forms.Padding(4);
            this.btnOpenFolderA.Name = "btnOpenFolderA";
            this.btnOpenFolderA.Size = new System.Drawing.Size(123, 26);
            this.btnOpenFolderA.TabIndex = 0;
            this.btnOpenFolderA.Text = "Open folder";
            this.btnOpenFolderA.UseVisualStyleBackColor = true;
            this.btnOpenFolderA.Click += new System.EventHandler(this.btnOpenFolderA_Click);
            // 
            // txtFolderA
            // 
            this.txtFolderA.Location = new System.Drawing.Point(87, 29);
            this.txtFolderA.Margin = new System.Windows.Forms.Padding(4);
            this.txtFolderA.Name = "txtFolderA";
            this.txtFolderA.Size = new System.Drawing.Size(502, 26);
            this.txtFolderA.TabIndex = 1;
            this.txtFolderA.KeyDown += new System.Windows.Forms.KeyEventHandler(this.txtFolderA_KeyDown);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 18);
            this.label1.TabIndex = 2;
            this.label1.Text = "Folder A";
            // 
            // groupBoxFolders
            // 
            this.groupBoxFolders.BackColor = System.Drawing.Color.White;
            this.groupBoxFolders.Controls.Add(this.radioCreationTime);
            this.groupBoxFolders.Controls.Add(this.radioAssembly);
            this.groupBoxFolders.Controls.Add(this.btnRefresh);
            this.groupBoxFolders.Controls.Add(this.checkColours);
            this.groupBoxFolders.Controls.Add(this.checkHide);
            this.groupBoxFolders.Controls.Add(this.label2);
            this.groupBoxFolders.Controls.Add(this.btnOpenFolderB);
            this.groupBoxFolders.Controls.Add(this.txtFolderB);
            this.groupBoxFolders.Controls.Add(this.label1);
            this.groupBoxFolders.Controls.Add(this.btnOpenFolderA);
            this.groupBoxFolders.Controls.Add(this.txtFolderA);
            this.groupBoxFolders.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBoxFolders.Location = new System.Drawing.Point(10, 10);
            this.groupBoxFolders.Margin = new System.Windows.Forms.Padding(5);
            this.groupBoxFolders.Name = "groupBoxFolders";
            this.groupBoxFolders.Size = new System.Drawing.Size(737, 186);
            this.groupBoxFolders.TabIndex = 3;
            this.groupBoxFolders.TabStop = false;
            this.groupBoxFolders.Text = "Settings";
            // 
            // checkColours
            // 
            this.checkColours.AutoSize = true;
            this.checkColours.Location = new System.Drawing.Point(333, 151);
            this.checkColours.Name = "checkColours";
            this.checkColours.Size = new System.Drawing.Size(120, 22);
            this.checkColours.TabIndex = 8;
            this.checkColours.Text = "Show colours";
            this.checkColours.UseVisualStyleBackColor = true;
            this.checkColours.CheckedChanged += new System.EventHandler(this.checkColours_CheckedChanged);
            // 
            // checkHide
            // 
            this.checkHide.AutoSize = true;
            this.checkHide.Location = new System.Drawing.Point(333, 123);
            this.checkHide.Name = "checkHide";
            this.checkHide.Size = new System.Drawing.Size(153, 22);
            this.checkHide.TabIndex = 7;
            this.checkHide.Text = "Hide inequal? Dlls";
            this.checkHide.UseVisualStyleBackColor = true;
            this.checkHide.CheckedChanged += new System.EventHandler(this.checkHide_CheckedChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(16, 83);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(68, 18);
            this.label2.TabIndex = 5;
            this.label2.Text = "Folder B";
            // 
            // btnOpenFolderB
            // 
            this.btnOpenFolderB.Location = new System.Drawing.Point(597, 80);
            this.btnOpenFolderB.Margin = new System.Windows.Forms.Padding(4);
            this.btnOpenFolderB.Name = "btnOpenFolderB";
            this.btnOpenFolderB.Size = new System.Drawing.Size(123, 26);
            this.btnOpenFolderB.TabIndex = 3;
            this.btnOpenFolderB.Text = "Open folder";
            this.btnOpenFolderB.UseVisualStyleBackColor = true;
            this.btnOpenFolderB.Click += new System.EventHandler(this.btnOpenFolderB_Click);
            // 
            // txtFolderB
            // 
            this.txtFolderB.Location = new System.Drawing.Point(87, 80);
            this.txtFolderB.Margin = new System.Windows.Forms.Padding(4);
            this.txtFolderB.Name = "txtFolderB";
            this.txtFolderB.Size = new System.Drawing.Size(502, 26);
            this.txtFolderB.TabIndex = 4;
            this.txtFolderB.KeyDown += new System.Windows.Forms.KeyEventHandler(this.txtFolderB_KeyDown);
            // 
            // gridDllCompare
            // 
            this.gridDllCompare.AllowUserToAddRows = false;
            this.gridDllCompare.AllowUserToDeleteRows = false;
            this.gridDllCompare.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.gridDllCompare.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.colDll,
            this.colFolderA,
            this.colFolderB});
            this.gridDllCompare.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.gridDllCompare.Location = new System.Drawing.Point(10, 206);
            this.gridDllCompare.Margin = new System.Windows.Forms.Padding(5);
            this.gridDllCompare.Name = "gridDllCompare";
            this.gridDllCompare.ReadOnly = true;
            this.gridDllCompare.RowHeadersVisible = false;
            this.gridDllCompare.Size = new System.Drawing.Size(737, 407);
            this.gridDllCompare.TabIndex = 4;
            // 
            // btnRefresh
            // 
            this.btnRefresh.Location = new System.Drawing.Point(597, 123);
            this.btnRefresh.Margin = new System.Windows.Forms.Padding(4);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(123, 50);
            this.btnRefresh.TabIndex = 9;
            this.btnRefresh.Text = "Refresh";
            this.btnRefresh.UseVisualStyleBackColor = true;
            this.btnRefresh.Click += new System.EventHandler(this.btnRefresh_Click);
            // 
            // radioAssembly
            // 
            this.radioAssembly.AutoSize = true;
            this.radioAssembly.Checked = true;
            this.radioAssembly.Location = new System.Drawing.Point(107, 123);
            this.radioAssembly.Name = "radioAssembly";
            this.radioAssembly.Size = new System.Drawing.Size(151, 22);
            this.radioAssembly.TabIndex = 10;
            this.radioAssembly.TabStop = true;
            this.radioAssembly.Text = "Assembly Version";
            this.radioAssembly.UseVisualStyleBackColor = true;
            this.radioAssembly.CheckedChanged += new System.EventHandler(this.radioAssembly_CheckedChanged);
            // 
            // radioCreationTime
            // 
            this.radioCreationTime.AutoSize = true;
            this.radioCreationTime.Location = new System.Drawing.Point(107, 151);
            this.radioCreationTime.Name = "radioCreationTime";
            this.radioCreationTime.Size = new System.Drawing.Size(124, 22);
            this.radioCreationTime.TabIndex = 11;
            this.radioCreationTime.Text = "Creation Time";
            this.radioCreationTime.UseVisualStyleBackColor = true;
            this.radioCreationTime.CheckedChanged += new System.EventHandler(this.radioCreationTime_CheckedChanged);
            // 
            // colDll
            // 
            this.colDll.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.Fill;
            this.colDll.FillWeight = 70F;
            this.colDll.HeaderText = "Dll";
            this.colDll.Name = "colDll";
            this.colDll.ReadOnly = true;
            // 
            // colFolderA
            // 
            this.colFolderA.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.Fill;
            this.colFolderA.FillWeight = 30F;
            this.colFolderA.HeaderText = "Folder A";
            this.colFolderA.Name = "colFolderA";
            this.colFolderA.ReadOnly = true;
            // 
            // colFolderB
            // 
            this.colFolderB.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.Fill;
            this.colFolderB.FillWeight = 30F;
            this.colFolderB.HeaderText = "Folder B";
            this.colFolderB.Name = "colFolderB";
            this.colFolderB.ReadOnly = true;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(60)))), ((int)(((byte)(73)))));
            this.ClientSize = new System.Drawing.Size(757, 623);
            this.Controls.Add(this.gridDllCompare);
            this.Controls.Add(this.groupBoxFolders);
            this.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Main";
            this.Padding = new System.Windows.Forms.Padding(10);
            this.Text = "Main";
            this.Load += new System.EventHandler(this.Main_Load);
            this.groupBoxFolders.ResumeLayout(false);
            this.groupBoxFolders.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.gridDllCompare)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnOpenFolderA;
        private System.Windows.Forms.TextBox txtFolderA;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBoxFolders;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnOpenFolderB;
        private System.Windows.Forms.TextBox txtFolderB;
        private System.Windows.Forms.DataGridView gridDllCompare;
        private System.Windows.Forms.CheckBox checkHide;
        private System.Windows.Forms.CheckBox checkColours;
        private System.Windows.Forms.Button btnRefresh;
        private System.Windows.Forms.RadioButton radioCreationTime;
        private System.Windows.Forms.RadioButton radioAssembly;
        private System.Windows.Forms.DataGridViewTextBoxColumn colDll;
        private System.Windows.Forms.DataGridViewTextBoxColumn colFolderA;
        private System.Windows.Forms.DataGridViewTextBoxColumn colFolderB;
    }
}

