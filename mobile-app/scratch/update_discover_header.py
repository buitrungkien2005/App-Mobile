import re

file = 'src/app/(tabs)/discover.tsx'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix layout: move header out of ScrollView
content = content.replace(
'''  return (
    <View style={styles.container}>
      
      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        
        {/* Header Section */}
        <View style={styles.headerContainer}>
          <Image 
            source={require('../../../assets/images/Lớp_phủ_trên_profiel.png')} 
            style={styles.overlay} 
            resizeMode="stretch" 
          />
          
          <View style={styles.headerContent}>
            {/* Top Row: Icons */}
            <View style={styles.topRow}>
              <View style={styles.rightIcons}>
                <TouchableOpacity style={styles.bellBtn}>
                  <Ionicons name="notifications" size={rs(18)} color="#000" />
                  <View style={styles.notificationDot} />
                </TouchableOpacity>
                <TouchableOpacity style={styles.avatarBtn} onPress={() => router.replace('/(tabs)/profile')}>
                  <Image source={require('../../../assets/images/discover-avatar.png')} style={styles.miniAvatar} />
                </TouchableOpacity>
                <TouchableOpacity style={styles.filterBtn}>
                  <Ionicons name="options-outline" size={rs(20)} color="#000" />
                </TouchableOpacity>
              </View>
            </View>

            {/* Absolute Logo */}
            <Image 
              source={require('../../../assets/images/BrandLogo.png')} 
              style={styles.logo} 
              resizeMode="contain" 
            />

            {/* Search Bar */}
            <View style={styles.searchWrapper}>
              <Ionicons name="search" size={rs(20)} color="#ffbb00" style={styles.searchIcon} />
              <TextInput 
                style={styles.searchInput}
                placeholder="Search contacts"
                placeholderTextColor="#9ca3af"
              />
            </View>
          </View>
        </View>''',
'''  return (
    <View style={styles.container}>
      
      {/* HEADER SECTION (Fixed) */}
      <View style={[styles.headerContainer, { height: OVERLAY_HEIGHT }]}>
        <Image 
          source={require('../../../assets/images/profile_overlay_new.png')} 
          style={[styles.overlay, { position: 'absolute', top: 0, left: 0, height: OVERLAY_HEIGHT }]} 
          resizeMode="cover" 
        />
        <View style={[styles.headerTop, { paddingTop: rs(65), position: 'relative' }]}>
          <Image source={require('../../../assets/images/BrandLogo.png')} style={styles.logoImage} resizeMode="contain" />
          
          <View style={styles.headerRightActions}>
            <TouchableOpacity style={styles.iconButton}>
              <Ionicons name="notifications" size={rs(18)} color="#000" />
              <View style={styles.notificationDot} />
            </TouchableOpacity>
            
            <TouchableOpacity style={styles.headerAvatarBtn} onPress={() => router.replace('/(tabs)/profile')}>
              <Image source={require('../../../assets/images/Avatar_Me.png')} style={styles.headerAvatar} />
            </TouchableOpacity>

            <TouchableOpacity style={styles.filterBtn}>
              <Ionicons name="options-outline" size={rs(20)} color="#000" />
            </TouchableOpacity>
          </View>
        </View>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        
        {/* Search Bar */}
        <View style={styles.searchSection}>
          <View style={styles.searchWrapper}>
            <Ionicons name="search" size={rs(20)} color="#ffbb00" style={styles.searchIcon} />
            <TextInput 
              style={styles.searchInput}
              placeholder="Search contacts"
              placeholderTextColor="#9ca3af"
            />
          </View>
        </View>'''
)

# Fix styles
content = content.replace(
'''  headerContainer: {
    width: '100%',
    marginBottom: rs(10),
  },
  overlay: {
    position: 'absolute',
    width: '100%',
    height: rs(100), // Fixed height so it doesn't cover everything
  },
  headerContent: {
    paddingHorizontal: rs(20),
    paddingTop: rs(90), // Push icons further below the overlay
  },
  topRow: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
    alignItems: 'center',
    marginBottom: rs(35), // Pushes search wrapper further down
  },
  logo: {
    position: 'absolute',
    top: rs(85),
    left: rs(20),
    width: rs(40),
    height: rs(60),
  },
  rightIcons: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  bellBtn: {
    width: rs(36),
    height: rs(36),
    borderRadius: rs(18),
    backgroundColor: '#ffbb00',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: rs(10),
  },
  notificationDot: {
    position: 'absolute',
    top: rs(6),
    right: rs(8),
    width: rs(8),
    height: rs(8),
    backgroundColor: '#ef4444',
    borderRadius: rs(4),
  },
  avatarBtn: {
    width: rs(36),
    height: rs(36),
    borderRadius: rs(18),
    borderWidth: 2,
    borderColor: '#ffbb00',
    overflow: 'hidden',
    marginRight: rs(10),
  },
  miniAvatar: {
    width: '100%',
    height: '100%',
  },''',
'''  headerContainer: {
    width: '100%',
  },
  overlay: {
    width: '100%',
  },
  headerTop: {
    width: '100%',
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: rs(20),
    alignItems: 'center',
  },
  logoImage: {
    height: rs(46),
    width: rs(30),
  },
  headerRightActions: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'flex-end',
  },
  iconButton: {
    width: rs(36),
    height: rs(36),
    borderRadius: rs(18),
    backgroundColor: '#ffb703',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: rs(10),
  },
  notificationDot: {
    position: 'absolute',
    top: rs(8),
    right: rs(10),
    width: rs(6),
    height: rs(6),
    backgroundColor: 'red',
    borderRadius: rs(3),
  },
  headerAvatarBtn: {
    width: rs(36),
    height: rs(36),
    borderRadius: rs(18),
    backgroundColor: '#ffb703',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: rs(10),
    borderWidth: 2,
    borderColor: '#ffb703',
    overflow: 'hidden',
  },
  headerAvatar: {
    width: rs(32),
    height: rs(32),
    borderRadius: rs(16),
  },
  searchSection: {
    paddingHorizontal: rs(20),
    marginTop: rs(20),
    marginBottom: rs(20),
  },'''
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
