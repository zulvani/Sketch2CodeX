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
      home: const TestDesktop4HandPazrinDssRunAhpResultS2cJson(),
    );
  }
}

class TestDesktop4HandPazrinDssRunAhpResultS2cJson extends StatelessWidget {
  const TestDesktop4HandPazrinDssRunAhpResultS2cJson({super.key});

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
                    const Spacer(flex: 10),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    Expanded(
                      flex: 11,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:table
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
                    const Spacer(flex: 1),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 3
                Row(
                  children: [

                    Expanded(
                      flex: 4,
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
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 8),

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 4,
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
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 4
                Row(
                  children: [

                    const Spacer(flex: 4),

                    Expanded(
                      flex: 2,
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
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 5
                Row(
                  children: [

                    Expanded(
                      flex: 10,
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

                    const Spacer(flex: 4),

                    Expanded(
                      flex: 2,
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
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 7
                Row(
                  children: [

                    const Spacer(flex: 3),

                    Expanded(
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:input-password
                              Expanded(
                                flex: 8,
                                child: TextField(
                                  obscureText: true,
                                  decoration: InputDecoration(
                                    hintText: 'Enter password',
                                    border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    contentPadding: const EdgeInsets.symmetric(
                                      horizontal: 12,
                                      vertical: 12,
                                    ),
                                  ),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 6),

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

