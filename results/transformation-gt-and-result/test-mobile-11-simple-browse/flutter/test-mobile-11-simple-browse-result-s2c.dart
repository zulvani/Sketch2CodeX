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
      home: const TestMobile11SimpleBrowseResultS2cJson(),
    );
  }
}

class TestMobile11SimpleBrowseResultS2cJson extends StatelessWidget {
  const TestMobile11SimpleBrowseResultS2cJson({super.key});

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
//obj:key-value
                              Expanded(
                                flex: 12,
                                child: Column(
                                  children: const [
                                    Row(
                                      children: [
                                        Expanded(child: Text('Key')),
                                        Expanded(child: Text('Value')),
                                      ],
                                    ),
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
                      flex: 12,
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

