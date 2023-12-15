class prefs:
    debug = 0  # デバッグモード
    miditrackname = 'Sample Track'  # MIDIトラック名
    notes_overlap = False  # (ノートのオーバーラップ設定)ノートが重なるかどうかの設定

    resize = 0  # リサイズの設定
    resize_width = 1280  # リサイズ後の幅
    resize_height = 720  # リサイズ後の高さ

    # ミニマルなデュレーションと無視の設定
    minimal_duration = 0.1  # ノートの最小長の設定
    ignore_minimal_duration = False  # 最小長を無視するかどうかの設定

    keyp_delta = 90  # キーポイントの感度

    octave = 3  # オクターブの設定
    tempo = 120  # テンポの設定
    startframe = 1  # 開始フレームの設定

    blackkey_relative_position = 0.4  # 黒鍵の相対位置

    keyp_spark_y_pos = -110  # キープレススパークのY座標
    use_sparks = False  # スパークを使用するかどうかの設定

    use_alternate_keys = False  # 代替キーを使用するかどうかの設定
    rollcheck = False  # ロールチェックの設定
    rollcheck_priority = 0  # ロールチェックの優先度

    # キーポイントの色（MIDIチャンネルごと）
    keyp_colors_channel = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]
    # MIDIプログラムID（チャンネルごと）
    keyp_colors_channel_prog = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # キーの位置設定
    xoffset_whitekeys = 60  # 白鍵のXオフセット
    yoffset_whitekeys = 673  # 白鍵のYオフセット
    yoffset_blackkeys = -30  # 黒鍵のYオフセット
    whitekey_width = 24.6  # 白鍵の幅

    keyp_colors_alternate = []  # 代替キーの色
    keyp_colors_alternate_sensitivity = []  # 代替キーの感度

    # キープレスの色
    keyp_colors = [
        # 明るい緑,暗い緑
        [166, 250, 103], [58, 146, 0],
        # 明るい青,暗い青
        [102, 185, 207], [8, 113, 174],
        # 明るい黄,暗い黄
        [255, 255, 85], [254, 210, 0],
        # 明るいオレンジ,暗いオレンジ
        [255, 212, 85], [255, 138, 0],
        # 明るい赤,暗い赤
        [253, 125, 114], [255, 37, 9],
        # 空白
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0]
    ]

    # キーポイントスパークの感度
    keyp_colors_sparks_sensitivity = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

    keys_pos = []  # キーの位置
    keys_angle = 90  # キーの角度

    use_percolor_delta = False  # 色ごとのパーカラーデルタを使用するかどうかの設定

    percolor_delta = [90] * 20  # 色ごとのパーカラーデルタの設定
    autoclose = 1  # オートクローズの設定
    sync_notes_start_pos = False  # ノートの開始位置を同期するかどうかの設定
    sync_notes_start_pos_time_delta = 1000  # ノートの開始位置を同期する時間差
    save_to_disk_message = ''  # ディスクに保存するメッセージ
    save_to_disk_per_channel = False  # チャンネルごとにディスクに保存するかどうかの設定
