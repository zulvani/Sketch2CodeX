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
      home: const TestMobile15BrowseProductsResultYolov11Json(),
    );
  }
}

class TestMobile15BrowseProductsResultYolov11Json extends StatelessWidget {
  const TestMobile15BrowseProductsResultYolov11Json({super.key});

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
//obj:input-file
                              Expanded(
                                flex: 8,
                                child: OutlinedButton.icon(
                                  onPressed: () {},
                                  icon: const Icon(Icons.attach_file),
                                  label: const Text('Attachment'),
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

                // Row 3
                Row(
                  children: [

                    Expanded(
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:common-button
                              Expanded(
                                flex: 4,
                                child: SizedBox(
                                  height: 45,
                                  child: ElevatedButton(
                                    onPressed: () {},
                                    child: const Text('Button'),
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
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:common-button
                              Expanded(
                                flex: 4,
                                child: SizedBox(
                                  height: 45,
                                  child: ElevatedButton(
                                    onPressed: () {},
                                    child: const Text('Button'),
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
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:common-image-button
                              Expanded(
                                flex: 4,
                                child: SizedBox(
                                  height: 45,
                                  child: ElevatedButton.icon(
                                    onPressed: () {},
                                    icon: const Icon(Icons.image),
                                    label: const Text('Button'),
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
                      flex: 3,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:common-button
                              Expanded(
                                flex: 4,
                                child: SizedBox(
                                  height: 45,
                                  child: ElevatedButton(
                                    onPressed: () {},
                                    child: const Text('Button'),
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

                // Row 4
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
                        ],
                      ),
                    ),
                    const Spacer(flex: 8),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 5
                Row(
                  children: [

                    Expanded(
                      flex: 3,
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
                    const Spacer(flex: 9),

                    Expanded(
                      flex: 3,
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
                    const Spacer(flex: 9),

                    Expanded(
                      flex: 3,
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
                    const Spacer(flex: 9),

                    Expanded(
                      flex: 3,
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
                    const Spacer(flex: 9),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 6
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
                        ],
                      ),
                    ),
                    const Spacer(flex: 8),

                    const Spacer(flex: 6),

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
                    const Spacer(flex: 4),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 7
                Row(
                  children: [

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
                        ],
                      ),
                    ),
                    const Spacer(flex: 6),

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
                        ],
                      ),
                    ),
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 8
                Row(
                  children: [

                    Expanded(
                      flex: 12,
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
                  ],
                ),

                const SizedBox(height: 16),

                // Row 9
                Row(
                  children: [

                    Expanded(
                      flex: 4,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:combobox
                              Expanded(
                                flex: 8,
                                child: DropdownButtonFormField<String>(
                                  value: null,
                                  items: const [
                                    DropdownMenuItem(value: 'Option 1', child: Text('Option 1')),
                                    DropdownMenuItem(value: 'Option 2', child: Text('Option 2')),
                                  ],
                                  onChanged: (v) {},
                                  decoration: InputDecoration(
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
                    const Spacer(flex: 8),

                    Expanded(
                      flex: 3,
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
                    const Spacer(flex: 9),

                    Expanded(
                      flex: 5,
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
                    const Spacer(flex: 7),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 10
                Row(
                  children: [

                    Expanded(
                      flex: 2,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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
//obj:icon-button
                              Expanded(
                                flex: 2,
                                child: IconButton(
                                  onPressed: () {},
                                  icon: const Icon(Icons.play_arrow),
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

