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
      home: const TestDesktop10BrowseProductResultSdnJson(),
    );
  }
}

class TestDesktop10BrowseProductResultSdnJson extends StatelessWidget {
  const TestDesktop10BrowseProductResultSdnJson({super.key});

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

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    Expanded(
                      flex: 4,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:input-free-text
                              Expanded(
                                flex: 8,
                                child: TextField(
                                  decoration: InputDecoration(
                                    hintText: 'Enter text',
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
                    const Spacer(flex: 8),

                    Expanded(
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:date-picker
                              Expanded(
                                flex: 8,
                                child: TextField(
                                  readOnly: true,
                                  decoration: InputDecoration(
                                    hintText: 'Select date',
                                    suffixIcon: const Icon(Icons.calendar_today),
                                    border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                  ),
                                ),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 9),

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:time-picker
                              Expanded(
                                flex: 8,
                                child: TextField(
                                  readOnly: true,
                                  decoration: InputDecoration(
                                    hintText: 'Select time',
                                    suffixIcon: const Icon(Icons.access_time),
                                    border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
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

                // Row 3
                Row(
                  children: [

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
                          const SizedBox(height: 16),
                          Row(
                            children: [
//obj:checkbox
                              Expanded(
                                flex: 1,
                                child: Checkbox(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                          const SizedBox(height: 16),
                          Row(
                            children: [
//obj:checkbox
                              Expanded(
                                flex: 1,
                                child: Checkbox(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                          const SizedBox(height: 16),
                          Row(
                            children: [
//obj:switch
                              Expanded(
                                flex: 2,
                                child: Switch(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 8),

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
                          const SizedBox(height: 16),
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

                    Expanded(
                      flex: 2,
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
                          const SizedBox(height: 16),
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
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 10),

                    Expanded(
                      flex: 6,
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
                          const SizedBox(height: 16),
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
                          const SizedBox(height: 16),
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
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 6),

                    Expanded(
                      flex: 2,
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
                          const SizedBox(height: 16),
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
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 10),

                    Expanded(
                      flex: 2,
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
                          const SizedBox(height: 16),
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
                          const SizedBox(height: 16),
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
                    const Spacer(flex: 10),

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

