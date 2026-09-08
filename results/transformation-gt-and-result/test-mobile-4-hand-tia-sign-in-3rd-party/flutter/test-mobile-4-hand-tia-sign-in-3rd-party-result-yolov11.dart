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
      home: const TestMobile4HandTiaSignIn3rdPartyResultYolov11Json(),
    );
  }
}

class TestMobile4HandTiaSignIn3rdPartyResultYolov11Json extends StatelessWidget {
  const TestMobile4HandTiaSignIn3rdPartyResultYolov11Json({super.key});

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

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 7,
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
                    const Spacer(flex: 3),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 4,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:undefined
                              Expanded(
                                flex: 12,
                                child: const Text('Unknown Object'),
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

                // Row 3
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 7,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:undefined
                              Expanded(
                                flex: 12,
                                child: const Text('Unknown Object'),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 3),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 4
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 7,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:undefined
                              Expanded(
                                flex: 12,
                                child: const Text('Unknown Object'),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 3),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 5
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 7,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:undefined
                              Expanded(
                                flex: 12,
                                child: const Text('Unknown Object'),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 3),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 6
                Row(
                  children: [

                    const Spacer(flex: 2),

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
                    const Spacer(flex: 9),

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 5,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:undefined
                              Expanded(
                                flex: 12,
                                child: const Text('Unknown Object'),
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

