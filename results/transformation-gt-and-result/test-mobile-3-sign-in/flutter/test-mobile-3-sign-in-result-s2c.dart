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
      home: const TestMobile3SignInResultS2cJson(),
    );
  }
}

class TestMobile3SignInResultS2cJson extends StatelessWidget {
  const TestMobile3SignInResultS2cJson({super.key});

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
                    const Spacer(flex: 6),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 2
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 8,
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
                    const Spacer(flex: 2),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 3
                Row(
                  children: [

                    const Spacer(flex: 2),

                    Expanded(
                      flex: 8,
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
                    const Spacer(flex: 2),

                  ],
                ),

                const SizedBox(height: 16),

                // Row 4
                Row(
                  children: [

                    const Spacer(flex: 4),

                    Expanded(
                      flex: 4,
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
                    const Spacer(flex: 4),

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
//obj:hyperlink
                              Expanded(
                                flex: 8,
                                child: Center(
                                  child: TextButton(
                                    onPressed: () {},
                                    child: const Text('Hyperlink'),
                                  ),
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
//obj:checkbox
                              Expanded(
                                flex: 1,
                                child: Checkbox(value: true, onChanged: (v) {}),
                              ),

                            ],
                          ),
                        ],
                      ),
                    ),
                    const Spacer(flex: 9),

                    const Spacer(flex: 1),

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
                    const Spacer(flex: 7),

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

