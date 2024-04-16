#使用：WordPressの表を自動生成
#項目を入れたら、全てhtmlで表示
#IT転職エージェントの表で使える


import streamlit as st

def main():
    st.title("表作成システム")

    # 運営会社の入力
    company = st.text_input("運営会社を入力してください")
    permission_number = st.text_input("ここに運営会社の事業許可番号の数字を入力してください")
    permission_url = st.text_input("事業許可番号のURLを入力してください")

    # 非公開求人の入力
    closed_jobs = st.text_input("ここに非公開求人について入力してください（件数 or 非公開）")

    # 職種の検索機能の入力
    job_search = st.text_area("ここに職種の検索機能を入力してください")

    # スキル・資格一覧の検索機能の入力
    skill_search = st.text_area("ここにスキル・資格一覧の検索機能を入力してください")

    # 対応エリアの入力
    area = st.text_area("ここに対応エリアを入力してください")

    # サービスの特徴の入力
    features = []
    for i in range(3):
        feature = st.text_input(f"サービスの特徴{i+1}を入力してください")
        features.append(feature)

    # 特徴の追加ボタン
    if st.button("もっと特徴を追加する"):
        feature = st.text_input(f"サービスの特徴{len(features)+1}を入力してください")
        features.append(feature)

    # 公式サイトのURLの入力
    official_url = st.text_input("ここに公式サイトのURLを挿入してください")

    # アフィリエイトリンクの入力
    affiliate_url = st.text_input("アフィリエイトリンクをここに挿入してください")

    # 完了ボタンが押されたら表のHTMLコードを生成
    if st.button("完了"):
        table_html = generate_table_html(company, permission_number, permission_url, closed_jobs, job_search, skill_search, area, features, official_url, affiliate_url)
        st.code(table_html, language='html')

def generate_table_html(company, permission_number, permission_url, closed_jobs, job_search, skill_search, area, features, official_url, affiliate_url):
    feature_html = ""
    for feature in features:
        if feature:
            feature_html += f'<span class="point-orenge">{feature}</span>\n'

    table_html = f'''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css">
<figure class="wp-block-table min_width30_ is-all-centered--va sp_block_">
  <table>
    <tbody>
      <tr>
        <th style="text-align:center;">運営会社</th>
        <td>{company}<br>(<a href="{permission_url}">職業紹介事業許可番号：{permission_number}</a>)</td>
      </tr>
      <tr>
        <th style="text-align:center;">公開求人数<br>2024年時点</th>
        <td>{closed_jobs}</td>
      </tr>
      <tr>
        <th style="text-align:center;">検索機能<br>職種</th>
        <td>
          <details>
            <summary><i class="fas fa-briefcase"></i> 職種一覧を開く</summary>
            {job_search}
          </details>
        </td>
      </tr>
      <tr>
        <th style="text-align:center;">検索機能<br>スキル・資格</th>
        <td>
          <details>
            <summary><i class="fas fa-wrench"></i> スキル・資格一覧を開く</summary>
            {skill_search}
          </details>
        </td>
      </tr>
      <tr>
        <th style="text-align:center;">対応エリア</th>
        <td>
          <details>
            <summary><i class="fas fa-map-marker-alt"></i> 対応エリア一覧を開く</summary>
            {area}
          </details>
        </td>
      </tr>
      <tr>
        <th style="text-align:center;">ポイント</th>
        <td>
          {feature_html}
        </td>
      </tr>
      <tr>
        <th style="text-align:center;">公式URL</th>
        <td><a rel="nofollow" href="{affiliate_url}">{official_url}</a></td>
      </tr>
    </tbody>
  </table>
</figure>
'''

    return table_html

if __name__ == "__main__":
    main()
