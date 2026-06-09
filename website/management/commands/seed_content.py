from django.core.management.base import BaseCommand
from website.models import (
    Theme, CoreValue, Accreditation, InterventionLevel,
    Location, Activity, TeamRole, ImpactStory,
)


class Command(BaseCommand):
    help = 'Seed initial data for all new content models'

    def handle(self, *args, **options):
        self._themes()
        self._values()
        self._accreditations()
        self._levels()
        self._locations()
        self._activities()
        self._team_roles()
        self._stories()
        self.stdout.write(self.style.SUCCESS('All content seeded successfully.'))

    def _themes(self):
        Theme.objects.all().delete()
        Theme.objects.bulk_create([
            Theme(icon='fa-solid fa-trophy', title='Trauma into Triumph', order=1, is_active=True,
                  description=(
                      'People come to KAI-K after going through traumatic experiences. '
                      'Through our intervention programs, they are supported to work through '
                      'what they have been through and move toward victory. The goal is not '
                      'just survival but triumph, where children and families come out the '
                      'other side stronger and able to live full, healthy lives.'
                  )),
            Theme(icon='fa-solid fa-scale-balanced', title='Justice that Heals', order=2, is_active=True,
                  description=(
                      'Justice that Heals treats children and families with compassion while '
                      'holding offenders accountable. It gives survivors a path to heal, '
                      'strengthens communities, and leads to better outcomes in the legal '
                      'system. We believe that without justice, healing is delayed or may '
                      'never fully come.'
                  )),
            Theme(icon='fa-solid fa-heart-pulse', title='Bonds that Mend', order=3, is_active=True,
                  description=(
                      'Every child needs a strong bond with a safe, loving, and caring adult. '
                      'Without safety, children experience trauma. Without love, they form '
                      'broken identities. Without nurturing, they struggle to grow. We work '
                      'to build these bonds in every family, classroom, and interaction, '
                      'because healing starts with connection.'
                  )),
        ])
        self.stdout.write('  Themes: %d' % Theme.objects.count())

    def _values(self):
        CoreValue.objects.all().delete()
        CoreValue.objects.bulk_create([
            CoreValue(icon='fa-solid fa-cross', title='Faith', order=1, is_active=True,
                      description='Rooted in Christian faith and the belief that every child is cherished by God.'),
            CoreValue(icon='fa-solid fa-shield-halved', title='Integrity', order=2, is_active=True,
                      description='Accountable to the children, families, and communities we serve, and to God.'),
            CoreValue(icon='fa-solid fa-brain', title='Understanding', order=3, is_active=True,
                      description='Meeting every child and family where they are, with empathy and evidence-based care.'),
            CoreValue(icon='fa-solid fa-scale-balanced', title='Justice', order=4, is_active=True,
                      description='Seeking justice for every child — holding offenders accountable and advocating for systemic change.'),
            CoreValue(icon='fa-solid fa-mountain-sun', title='Perseverance', order=5, is_active=True,
                      description="We do the hard things. We go where others won't, and we stay as long as it takes."),
            CoreValue(icon='fa-solid fa-handshake', title='Mutual Kindness', order=6, is_active=True,
                      description='Treating every person with dignity, care, and the love of Christ in all our interactions.'),
        ])
        self.stdout.write('  Core Values: %d' % CoreValue.objects.count())

    def _accreditations(self):
        Accreditation.objects.all().delete()
        Accreditation.objects.bulk_create([
            Accreditation(icon='fa-solid fa-star', icon_color='#f59e0b',
                          name='Charity Navigator', subtitle='Four-Star Rating', order=1, is_active=True),
            Accreditation(icon='fa-solid fa-medal', icon_color='#a855f7',
                          name='GuideStar', subtitle='Platinum Seal of Transparency', order=2, is_active=True),
            Accreditation(icon='fa-solid fa-check-double', icon_color='var(--color-primary)',
                          name='ECFA', subtitle='Evangelical Council for Financial Accountability',
                          order=3, is_active=True),
        ])
        self.stdout.write('  Accreditations: %d' % Accreditation.objects.count())

    def _levels(self):
        InterventionLevel.objects.all().delete()
        InterventionLevel.objects.bulk_create([
            InterventionLevel(icon='fa-solid fa-graduation-cap', title='Restorative Education',
                              order=1, is_active=True, location='Nyeri County',
                              description=(
                                  'We run education and training programs in settings that support '
                                  'healing while children learn. Hall Mead School in Nyeri County '
                                  'provides a caring environment that supports children\'s academic, '
                                  'social, spiritual, and physical development.'
                              )),
            InterventionLevel(icon='fa-solid fa-people-roof', title='Family Strengthening',
                              order=2, is_active=True, location='Nairobi, Nyeri & Kisii Counties',
                              description=(
                                  'We work with families to reduce the risks they face and help them '
                                  'grow stronger. Through our Hope Centres in Nairobi, Karundas, and '
                                  'Nyamarambe, we provide parenting support, psychosocial education, '
                                  'livelihood training, and mentorship.'
                              )),
            InterventionLevel(icon='fa-solid fa-shield-halved', title='Protective Care',
                              order=3, is_active=True, location='All locations',
                              description=(
                                  'When a child has been abused or neglected and cannot safely stay at '
                                  'home, we provide temporary care. Our staff work to meet each child\'s '
                                  'needs for health, safety, and emotional healing, with the goal of '
                                  'returning every child to a safe family environment.'
                              )),
            InterventionLevel(icon='fa-solid fa-scale-balanced', title='Justice Advocacy',
                              order=4, is_active=True, location='All locations',
                              description=(
                                  'We support children who have experienced abuse to access justice. Our '
                                  'teams include lawyers, psychologists, social workers, and spiritual '
                                  'leads who walk alongside the child and family through the legal '
                                  'process, and advocate for better laws at local, regional, and '
                                  'national levels.'
                              )),
            InterventionLevel(icon='fa-solid fa-kit-medical', title='Community Health',
                              order=5, is_active=True, location='Nyeri County',
                              description=(
                                  'KAI-K owns and operates a clinic in Nyeri County that provides '
                                  'medical services to the local community, in partnership with the '
                                  'Nyeri County Government.'
                              )),
            InterventionLevel(icon='fa-solid fa-chalkboard-user', title='Capacity Building',
                              order=6, is_active=True, location='All locations',
                              description=(
                                  'KAI-K partners with public and private schools, county governments, '
                                  'and institutions that work with children to provide capacity building '
                                  'for the adults in those settings. The training equips teachers, '
                                  'caregivers, and other staff with the knowledge and skills to care '
                                  'for children in a trauma-informed way.'
                              )),
        ])
        self.stdout.write('  Intervention Levels: %d' % InterventionLevel.objects.count())

    def _locations(self):
        Location.objects.all().delete()
        Location.objects.bulk_create([
            Location(badge='Nairobi County', name='Nairobi Hope Centre',
                     focus='Family Strengthening & Justice Advocacy', order=1, is_active=True),
            Location(badge='Nyeri County', name='Karundas Hope Centre',
                     focus='Family Strengthening & Justice Advocacy', order=2, is_active=True),
            Location(badge='Nyeri County', name='Hall Mead School',
                     focus='Restorative Education', order=3, is_active=True),
            Location(badge='Nyeri County', name='Nyeri Clinic',
                     focus='Community Health Services — in partnership with Nyeri County Government',
                     order=4, is_active=True),
            Location(badge='Kisii County', name='Nyamarambe Hope Centre',
                     focus='Family Strengthening & Justice Advocacy', order=5, is_active=True),
        ])
        self.stdout.write('  Locations: %d' % Location.objects.count())

    def _activities(self):
        Activity.objects.all().delete()
        Activity.objects.bulk_create([
            Activity(text='Therapeutic care and psychosocial support', order=1, is_active=True),
            Activity(text='Spiritual discipleship', order=2, is_active=True),
            Activity(text='Parenting skills training', order=3, is_active=True),
            Activity(text='Psychosocial education for children and caregivers', order=4, is_active=True),
            Activity(text='Mentorship skills training', order=5, is_active=True),
            Activity(text='Community awareness and justice advocacy', order=6, is_active=True),
            Activity(text='Livelihood training and support', order=7, is_active=True),
            Activity(text='Capacity building for teachers, church leaders, and staff at partner schools and institutions',
                     order=8, is_active=True),
            Activity(text='Linkages and partnerships with government and other organisations', order=9, is_active=True),
            Activity(text='Partial education support for children in the community', order=10, is_active=True),
        ])
        self.stdout.write('  Activities: %d' % Activity.objects.count())

    def _team_roles(self):
        TeamRole.objects.all().delete()
        TeamRole.objects.bulk_create([
            TeamRole(icon='fa-solid fa-gavel', title='Lawyers', order=1, is_active=True,
                     description='Provide legal representation for children in civil and criminal abuse cases.'),
            TeamRole(icon='fa-solid fa-brain', title='Psychologists', order=2, is_active=True,
                     description='Help children process trauma and prepare to give testimony in court, using the KAI toolkit.'),
            TeamRole(icon='fa-solid fa-people-group', title='Social Workers', order=3, is_active=True,
                     description="Support children and families through the justice process and work to ensure the child's ongoing safety."),
            TeamRole(icon='fa-solid fa-chalkboard-user', title='Teachers', order=4, is_active=True,
                     description='Deliver restorative, trauma-informed education in KAI-K classrooms, creating learning environments where children feel safe and supported.'),
            TeamRole(icon='fa-solid fa-cross', title='Spiritual Leads', order=5, is_active=True,
                     description='Provide faith-based discipleship and support spiritual formation as part of the healing process.'),
        ])
        self.stdout.write('  Team Roles: %d' % TeamRole.objects.count())

    def _stories(self):
        ImpactStory.objects.all().delete()
        ImpactStory.objects.bulk_create([
            ImpactStory(
                label="Linnet's Story",
                person_name='Linnet',
                name_note='Name changed to protect privacy',
                order=1, is_active=True,
                body=(
                    'Linnet came to KAI through a local health clinic after she and her family '
                    'experienced trauma. KAI enrolled Linnet, her younger sister, and her mother '
                    'in the program for emotional support. Linnet joined a KAI school and went on '
                    'to graduate with excellent final exam results. Her story shows what becomes '
                    'possible when a child receives consistent care and support.'
                ),
            ),
            ImpactStory(
                label="Ivy's Story",
                person_name='Ivy, age 14',
                name_note='Name changed to protect privacy',
                order=2, is_active=True,
                body=(
                    'Ivy, age 14, has lived with the effects of abandonment since birth. Neglect '
                    'left her guarded and avoidant. Through KAI-K\'s care, she has grown in '
                    'self-awareness and has started to form healthy connections with others. '
                    'KAI-K works with children like Ivy to help them rebuild trust and find their '
                    'footing in family and community.'
                ),
            ),
        ])
        self.stdout.write('  Impact Stories: %d' % ImpactStory.objects.count())
