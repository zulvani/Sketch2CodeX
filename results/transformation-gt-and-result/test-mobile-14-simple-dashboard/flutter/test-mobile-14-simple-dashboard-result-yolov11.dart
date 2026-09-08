import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const TestMobile14SimpleDashboardResultYolov11Json(),
    );
  }
}

class TestMobile14SimpleDashboardResultYolov11Json extends StatelessWidget {
  const TestMobile14SimpleDashboardResultYolov11Json({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade100,

      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(16),

            child: Column(
              children: [

                // Row 1
                Row(
                  children: [

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:list
                              Expanded(
                                flex: 12,
                                child: DataTable(
                                  columns: const [
                                    DataColumn(label: Text('Header 1')),
                                    DataColumn(label: Text('Header 2')),
                                  ],
                                  rows: const [
                                    DataRow(cells: [DataCell(Text('Cell 1')), DataCell(Text('Cell 2'))]),
                                  ],
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 10),

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:list
                              Expanded(
                                flex: 12,
                                child: DataTable(
                                  columns: const [
                                    DataColumn(label: Text('Header 1')),
                                    DataColumn(label: Text('Header 2')),
                                  ],
                                  rows: const [
                                    DataRow(cells: [DataCell(Text('Cell 1')), DataCell(Text('Cell 2'))]),
                                  ],
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 10),

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:list
                              Expanded(
                                flex: 12,
                                child: DataTable(
                                  columns: const [
                                    DataColumn(label: Text('Header 1')),
                                    DataColumn(label: Text('Header 2')),
                                  ],
                                  rows: const [
                                    DataRow(cells: [DataCell(Text('Cell 1')), DataCell(Text('Cell 2'))]),
                                  ],
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 10),

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:list
                              Expanded(
                                flex: 12,
                                child: DataTable(
                                  columns: const [
                                    DataColumn(label: Text('Header 1')),
                                    DataColumn(label: Text('Header 2')),
                                  ],
                                  rows: const [
                                    DataRow(cells: [DataCell(Text('Cell 1')), DataCell(Text('Cell 2'))]),
                                  ],
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 10),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    Expanded(
                      flex: 5,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:line-chart
                              Expanded(
                                flex: 12,
                                child: Container(
                                  height: 140,
                                  alignment: Alignment.center,
                                  decoration: BoxDecoration(
                                    color: Colors.white,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(color: Colors.grey.shade300),
                                  ),
                                  child: Text('line-chart'),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 7),

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 6,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:bar-chart
                              Expanded(
                                flex: 12,
                                child: Container(
                                  height: 140,
                                  alignment: Alignment.center,
                                  decoration: BoxDecoration(
                                    color: Colors.white,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(color: Colors.grey.shade300),
                                  ),
                                  child: Text('bar-chart'),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 5),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 3
                Row(
                  children: [

                    Expanded(
                      flex: 12,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:list
                              Expanded(
                                flex: 12,
                                child: DataTable(
                                  columns: const [
                                    DataColumn(label: Text('Header 1')),
                                    DataColumn(label: Text('Header 2')),
                                  ],
                                  rows: const [
                                    DataRow(cells: [DataCell(Text('Cell 1')), DataCell(Text('Cell 2'))]),
                                  ],
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 16),

                // Row 4
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 8,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:pie-chart
                              Expanded(
                                flex: 12,
                                child: Container(
                                  height: 140,
                                  alignment: Alignment.center,
                                  decoration: BoxDecoration(
                                    color: Colors.white,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(color: Colors.grey.shade300),
                                  ),
                                  child: Text('pie-chart'),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 2),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 5
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 8,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:slider
                              Expanded(
                                flex: 8,
                                child: Slider(value: 0.5, onChanged: (v) {}),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 2),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 6
                Row(
                  children: [

                    Expanded(
                      flex: 1,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:switch
                              Expanded(
                                flex: 2,
                                child: Switch(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 11),

                    Expanded(
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:label
                              Expanded(
                                flex: 4,
                                child: const Text(
                                  'Label',
                                  style: TextStyle(
                                    fontSize: 14,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 9),

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:label
                              Expanded(
                                flex: 4,
                                child: const Text(
                                  'Label',
                                  style: TextStyle(
                                    fontSize: 14,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 7),

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:switch
                              Expanded(
                                flex: 2,
                                child: Switch(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 9),

                  ],
                ),

              ],
            ),
          ),
        ),
      ),
    );
  }
}

