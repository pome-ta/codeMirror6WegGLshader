precision highp float;

uniform vec2 resolution;

out vec4 fragColor;

// コード 1.2:3 つのベクトルをつなぐ線形補間
void main(){
  vec2 pos = gl_FragCoord.xy / resolution.xy;

  vec3[3] col3 = vec3[](
    // ベクトルの配列
    vec3(1.0, 0.0, 0.0),
    vec3(0.0, 1.0, 0.0),
    vec3(0.0, 0.0, 1.0)
  );
  pos.x *= 2.0;//x 座標範囲を [0,2] 区間にスケール
  int ind = int(pos.x);// 配列のインデックス
  
  vec3 col = mix(col3[ind], col3[ind + 1], fract(pos.x));
  fragColor = vec4(col, 1.0);
}