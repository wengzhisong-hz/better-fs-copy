{
  "targets": [
    {
      "target_name": "binding",
      "sources": ["src/binding.cc"],
      "include_dirs" : [
          "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        [
          "OS=='win'",
          {
            "defines": [
              "_HAS_EXCEPTIONS=1"
            ],
            "msvs_settings": {
              "VCCLCompilerTool": {
                "ExceptionHandling": 1
              }
            }
          }
        ],
        [
          "OS=='mac'",
          {
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "CLANG_CXX_LIBRARY": "libc++",
              "MACOSX_DEPLOYMENT_TARGET": "10.7"
            }
          }
        ]
      ]
    }
  ]
}