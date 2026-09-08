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
      home: const TestMobile12HandPazrinBtpnsKoreksiTransaksiResultYolov11Json(),
    );
  }
}

class TestMobile12HandPazrinBtpnsKoreksiTransaksiResultYolov11Json extends StatelessWidget {
  const TestMobile12HandPazrinBtpnsKoreksiTransaksiResultYolov11Json({super.key});

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
                      flex: 5,
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
                    const Spacer(flex: 7),

                    const Spacer(flex: 2),

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

                // Row 2
                Row(
                  children: [

                    Expanded(
                      flex: 5,
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

