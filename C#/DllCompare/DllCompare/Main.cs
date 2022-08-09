using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading;
using System.Windows.Forms;

namespace DllCompare
{
    public partial class Main : Form
    {

        private List<string> folderAFiles;
        private List<string> folderBFiles;

        public Main()
        {
            InitializeComponent();
        }

        private void Main_Load(object sender, EventArgs e)
        {
            this.Text = Common.PROGRAM_NAME;

            folderAFiles = new List<string>();
            folderBFiles = new List<string>();

            gridDllCompare.ColumnHeadersDefaultCellStyle.BackColor = Common.Apicom_Blue_1;
            gridDllCompare.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;

#if DEBUG
            txtFolderA.Text = @"E:\EASYFlex and Beckoff Update\BeckhoffADS";
            txtFolderB.Text = @"E:\EASYFlex and Beckoff Update\EASYFlex_Engine";
#endif
        }

        private void btnOpenFolderA_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                txtFolderA.Text = fbd.SelectedPath;
                folderAFiles = GetDllsFromPath(txtFolderA.Text);
                RunComparison();
            }
        }

        private void btnOpenFolderB_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                txtFolderB.Text = fbd.SelectedPath;
                folderBFiles = GetDllsFromPath(txtFolderB.Text);
                RunComparison();
            }
        }

        private void RunComparison()
        {
            try
            {
                // Clear grid
                gridDllCompare.Rows.Clear();

                // Get files
                if (folderAFiles.Count <= 0 && folderBFiles.Count <= 0)
                {
                    folderAFiles = GetDllsFromPath(txtFolderA.Text);
                    folderBFiles = GetDllsFromPath(txtFolderB.Text);
                }

                // Display column header as folder
                DirectoryInfo infoA = new DirectoryInfo(txtFolderA.Text);
                gridDllCompare.Columns[1].HeaderText = infoA.Name;
                DirectoryInfo infoB = new DirectoryInfo(txtFolderB.Text);
                gridDllCompare.Columns[2].HeaderText = infoB.Name;

                // Display Dlls from folder A
                if (folderAFiles.Count > 0)
                {
                    foreach (string dll in folderAFiles)
                    {
                        DataGridViewRow newRow = new DataGridViewRow();
                        newRow.CreateCells(gridDllCompare);
                        newRow.Cells[0].Value = Path.GetFileName(dll);
                        newRow.Cells[1].Value = GetValue(dll);
                        gridDllCompare.Rows.Add(newRow);
                    }
                }

                // Display Dlls from folder B
                if (folderBFiles.Count > 0)
                {
                    foreach (string dll in folderBFiles)
                    {
                        int rowIndex = GetRowIndex(Path.GetFileName(dll));
                        if (rowIndex >= 0)
                        {
                            gridDllCompare.Rows[rowIndex].Cells[2].Value = GetValue(dll);
                        }
                        else
                        {
                            DataGridViewRow newRow = new DataGridViewRow();
                            newRow.CreateCells(gridDllCompare);
                            newRow.Cells[0].Value = Path.GetFileName(dll);
                            newRow.Cells[2].Value = FileVersionInfo.GetVersionInfo(dll).FileVersion;
                            gridDllCompare.Rows.Add(newRow);
                        }
                    }
                }

                // Filters (colours and hide Dlls only exist in one folder
                ApplyFilters();

            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error caught: {ex.Message}", Common.PROGRAM_NAME, MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private string GetValue(string dll)
        {
            if (radioAssembly.Checked)
            {
                return FileVersionInfo.GetVersionInfo(dll).FileVersion;
            }
            else if (radioCreationTime.Checked)
            {
                return File.GetCreationTime(dll).ToString("yyyy-MM-dd HH:mm:ss");
            }
            else
            {
                return "Error";
            }
        }

        private int GetRowIndex(string dllname)
        {
            foreach (DataGridViewRow row in gridDllCompare.Rows)
            {
                if (row.Cells[0].Value != null)
                {
                    if (row.Cells[0].Value.ToString().Equals(dllname))
                    {
                        return row.Index;
                    }
                }
            }
            return -1;
        }

        private List<string> GetDllsFromPath(string path)
        {
            if (Directory.Exists(path))
            {
                return Directory.GetFiles(path, "*.dll").ToList();
            }
            return null;
        }

        private void ApplyFilters()
        {
            if (checkHide.Checked)
            {
                List<DataGridViewRow> toRemove = new List<DataGridViewRow>();
                foreach (DataGridViewRow row in gridDllCompare.Rows)
                {
                    Console.WriteLine($"Processing {row.Cells[0].Value}");

                    if ((row.Cells[1].Value == null || string.IsNullOrEmpty(row.Cells[1].Value.ToString())) ||
                        (row.Cells[2].Value == null || string.IsNullOrEmpty(row.Cells[2].Value.ToString())))
                    {
                        toRemove.Add(row);
                        Console.WriteLine($"Removing {row.Cells[0].Value}");
                        continue;
                    }
                }
                toRemove.ForEach(x => gridDllCompare.Rows.Remove(x));
            }
            if (checkColours.Checked)
            {
                foreach (DataGridViewRow row in gridDllCompare.Rows)
                {

                    if (row.Cells[1].Value != null && row.Cells[2].Value != null)
                    {
                        if (row.Cells[1].Value.ToString().Equals(row.Cells[2].Value.ToString()))
                        {
                            row.DefaultCellStyle.BackColor = Common.Green;
                            row.DefaultCellStyle.SelectionForeColor = Color.White;
                            row.DefaultCellStyle.SelectionBackColor = Common.Green;
                            Console.WriteLine($"{row.Cells[0].Value}: both equal");
                            continue;
                        }
                        else
                        {
                            row.DefaultCellStyle.BackColor = Common.Red;
                            row.DefaultCellStyle.SelectionForeColor = Color.White;
                            row.DefaultCellStyle.SelectionBackColor = Common.Red;
                            Console.WriteLine($"{row.Cells[0].Value}: not equal");
                            continue;
                        }
                    }
                }
            }
            gridDllCompare.Refresh();
        }

        private void txtFolderA_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                RunComparison();
            }
        }

        private void txtFolderB_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                RunComparison();
            }
        }

        private void checkHide_CheckedChanged(object sender, EventArgs e)
        {
            RunComparison();
        }

        private void checkColours_CheckedChanged(object sender, EventArgs e)
        {
            RunComparison();
        }

        private void btnRefresh_Click(object sender, EventArgs e)
        {
            RunComparison();
        }

        private void radioAssembly_CheckedChanged(object sender, EventArgs e)
        {
            RunComparison();
        }

        private void radioCreationTime_CheckedChanged(object sender, EventArgs e)
        {
            RunComparison();
        }
    }
}
