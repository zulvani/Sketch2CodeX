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
      home: const TestMobile11HandAgusSimpleBrowseResultYolov11Json(),
    );
  }
}

class TestMobile11HandAgusSimpleBrowseResultYolov11Json extends StatelessWidget {
  const TestMobile11HandAgusSimpleBrowseResultYolov11Json({super.key});

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
                      flex: 12,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:image-card
                              Expanded(
                                flex: 12,
                                child: Card(
                                  clipBehavior: Clip.antiAlias,
                                  child: Column(
                                    mainAxisSize: MainAxisSize.min,
                                    children: const [
                                      SizedBox(height: 120, child: Center(child: Text('Image'))),
                                      Padding(
                                        padding: EdgeInsets.all(12),
                                        child: Text('Title'),
                                      ),
                                    ],
                                  ),
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

                // Row 2
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

                // Row 3
                Row(
                  children: [

                    Expanded(
                      flex: 11,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:segmented-button
                              Expanded(
                                flex: 8,
                                child: ToggleButtons(
                                  isSelected: const [true, false],
                                  onPressed: (index) {},
                                  children: const [
                                    Padding(
                                      padding: EdgeInsets.symmetric(horizontal: 12),
                                      child: Text('Button 1'),
                                    ),
                                    Padding(
                                      padding: EdgeInsets.symmetric(horizontal: 12),
                                      child: Text('Button 2'),
                                    ),
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

              ],
            ),
          ),
        ),
      ),
    );
  }
}

