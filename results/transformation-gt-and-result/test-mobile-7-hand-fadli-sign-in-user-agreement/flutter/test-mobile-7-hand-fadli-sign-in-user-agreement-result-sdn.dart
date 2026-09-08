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
      home: const TestMobile7HandFadliSignInUserAgreementResultSdnJson(),
    );
  }
}

class TestMobile7HandFadliSignInUserAgreementResultSdnJson extends StatelessWidget {
  const TestMobile7HandFadliSignInUserAgreementResultSdnJson({super.key});

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

                    const Spacer(flex: 1),

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
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 10,
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
                    const Spacer(flex: 1),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 3
                Row(
                  children: [

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 10,
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
                    const Spacer(flex: 1),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 4
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 6,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:alert
                              Expanded(
                                flex: 12,
                                child: Container(
                                  padding: const EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: Colors.orange.shade50,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(color: Colors.orange.shade200),
                                  ),
                                  child: const Row(
                                    children: [
                                      Icon(Icons.info_outline, color: Colors.orange),
                                      SizedBox(width: 8),
                                      Expanded(child: Text('Alert')),
                                    ],
                                  ),
                                ),
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

                // Row 5
                Row(
                  children: [

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 1,
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
                      flex: 8,
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
                    const Spacer(flex: 4),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 6
                Row(
                  children: [

                    const Spacer(flex: 1),

                    Expanded(
                      flex: 10,
                      child: Column(
                        children: [
                          Row(
                            children: [
//obj:textarea
                              Expanded(
                                flex: 8,
                                child: TextField(
                                  maxLines: 4,
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

