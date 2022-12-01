#include <napi.h>

Napi::String Method(const Napi::CallbackInfo &info)
{
  Napi::Env env = info.Env();
  return Napi::String::New(env, "hello");
}

Napi::Object Init(Napi::Env env, Napi::Object exports)
{
  exports.Set(Napi::String::New(env, "betterFsCopy"),
              Napi::Function::New(env, Method));
  return exports;
}

NODE_API_MODULE(betterFsCopy, Init)